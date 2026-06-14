import { expect, test } from "@playwright/test";

test("restores a shared calculator setup and submits it to the API", async ({
  context,
  page,
}) => {
  await context.grantPermissions(["clipboard-read", "clipboard-write"]);

  const requests: unknown[] = [];
  await page.route("**/api/vectors/add", async (route) => {
    requests.push(route.request().postDataJSON());
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify([12, 15, 18]),
    });
  });

  await page.goto("/calculator?cat=vectors&op=vec-add");

  await page.getByLabel("Vector A component 1").fill("8");
  await page.getByLabel("Vector A component 2").fill("9");
  await page.getByLabel("Vector A component 3").fill("10");
  await page.getByLabel("Vector B component 1").fill("4");
  await page.getByLabel("Vector B component 2").fill("6");
  await page.getByLabel("Vector B component 3").fill("8");

  await page.getByRole("button", { name: /share setup/i }).click();
  await expect(
    page.getByRole("button", { name: /link copied/i })
  ).toBeVisible();

  const sharedUrl = await page.evaluate(() => navigator.clipboard.readText());
  expect(sharedUrl).toContain("cat=vectors");
  expect(sharedUrl).toContain("op=vec-add");
  expect(sharedUrl).toContain("setup=");

  await page.goto(sharedUrl);

  await expect(page.getByRole("heading", { name: "Add" })).toBeVisible();
  await expect(page.getByLabel("Vector A component 1")).toHaveValue("8");
  await expect(page.getByLabel("Vector A component 2")).toHaveValue("9");
  await expect(page.getByLabel("Vector A component 3")).toHaveValue("10");
  await expect(page.getByLabel("Vector B component 1")).toHaveValue("4");
  await expect(page.getByLabel("Vector B component 2")).toHaveValue("6");
  await expect(page.getByLabel("Vector B component 3")).toHaveValue("8");

  await page.getByRole("button", { name: "Compute" }).click();

  await expect.poll(() => requests).toEqual([
    {
      vector1: [8, 9, 10],
      vector2: [4, 6, 8],
    },
  ]);
  await expect(
    page.getByTestId("result-panel").getByText("[12, 15, 18]", { exact: true })
  ).toBeVisible();

  await page.getByLabel("Vector A component 1").fill("99");
  await page.getByLabel("Vector B component 3").fill("1");
  await page.getByRole("button", { name: /use setup/i }).click();

  await expect(page.getByLabel("Vector A component 1")).toHaveValue("8");
  await expect(page.getByLabel("Vector B component 3")).toHaveValue("8");

  await page.getByRole("button", { name: "Compute" }).click();
  await expect.poll(() => requests).toEqual([
    {
      vector1: [8, 9, 10],
      vector2: [4, 6, 8],
    },
    {
      vector1: [8, 9, 10],
      vector2: [4, 6, 8],
    },
  ]);
});
