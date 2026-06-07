// Data-driven registry of every calculator operation exposed by the API.
// The UI is generated entirely from this file, so adding/adjusting an
// operation is a data edit, not a component change. Every operation is computed
// by the FastAPI backend via its `endpoint`.

export type FieldType =
  | "number" // float
  | "int" // integer
  | "text" // raw string (kept verbatim — used for high-precision operands & CAS)
  | "bool"
  | "vector" // number[]
  | "matrix" // number[][]
  | "textlist"; // string[] (one entry per line)

export type FieldValue =
  | string
  | boolean
  | number[]
  | number[][]
  | string[];

export interface Field {
  name: string;
  label: string;
  type: FieldType;
  help?: string;
  optional?: boolean;
  initial: FieldValue;
}

export interface QueryParam {
  name: string;
  label: string;
  type: "int" | "bool";
  initial: string | boolean;
  help?: string;
}

export type ResultKind =
  | "scalar"
  | "string"
  | "bool"
  | "vector"
  | "matrix"
  | "intlist"
  | "triples"
  | "triangle"
  | "table" // labelled rows: { label, value }[] (stats summary, base conversions)
  | "exprvector" // list of symbolic expression strings (e.g. gradient, curl)
  | "exprmatrix"; // grid of symbolic expression strings (e.g. hessian, jacobian)

// A labelled row for the "table" result kind.
export interface TableRow {
  label: string;
  value: string;
}

export interface Operation {
  id: string;
  label: string;
  blurb: string;
  endpoint: string;
  method?: "GET" | "POST";
  fields: Field[];
  query?: QueryParam[];
  result: ResultKind;
  resultLabel?: string;
}

export interface Category {
  id: string;
  label: string;
  tagline: string;
  operations: Operation[];
}

// ---- small field builders to keep the registry terse ----
const num = (name: string, label: string, initial = "", help?: string): Field => ({
  name,
  label,
  type: "number",
  initial,
  help,
});
const int = (name: string, label: string, initial = "", help?: string): Field => ({
  name,
  label,
  type: "int",
  initial,
  help,
});
const txt = (name: string, label: string, initial = "", help?: string): Field => ({
  name,
  label,
  type: "text",
  initial,
  help,
});
const vec = (name: string, label: string, initial: number[]): Field => ({
  name,
  label,
  type: "vector",
  initial,
});
const mat = (name: string, label: string, initial: number[][]): Field => ({
  name,
  label,
  type: "matrix",
  initial,
});
const tlist = (name: string, label: string, initial: string[], help?: string): Field => ({
  name,
  label,
  type: "textlist",
  initial,
  help,
});

const PRECISION: QueryParam = {
  name: "precision",
  label: "Precision (digits)",
  type: "int",
  initial: "50",
  help: "Number of significant digits to compute.",
};

export const CATEGORIES: Category[] = [
  // ===================== VECTORS =====================
  {
    id: "vectors",
    label: "Vectors",
    tagline: "Linear algebra in n dimensions",
    operations: [
      {
        id: "vec-add",
        label: "Add",
        blurb: "Component-wise sum of two equal-length vectors.",
        endpoint: "/vectors/add",
        fields: [vec("vector1", "Vector A", [1, 2, 3]), vec("vector2", "Vector B", [4, 5, 6])],
        result: "vector",
      },
      {
        id: "vec-sub",
        label: "Subtract",
        blurb: "Component-wise difference A − B.",
        endpoint: "/vectors/subtract",
        fields: [vec("vector1", "Vector A", [4, 5, 6]), vec("vector2", "Vector B", [1, 2, 3])],
        result: "vector",
      },
      {
        id: "vec-dot",
        label: "Dot product",
        blurb: "Scalar projection A · B.",
        endpoint: "/vectors/dot",
        fields: [vec("vector1", "Vector A", [1, 2, 3]), vec("vector2", "Vector B", [4, 5, 6])],
        result: "scalar",
      },
      {
        id: "vec-cross",
        label: "Cross product",
        blurb: "Perpendicular vector A × B (3-D only).",
        endpoint: "/vectors/cross",
        fields: [vec("vector1", "Vector A", [1, 0, 0]), vec("vector2", "Vector B", [0, 1, 0])],
        result: "vector",
      },
      {
        id: "vec-scale",
        label: "Scale",
        blurb: "Multiply every component by a scalar.",
        endpoint: "/vectors/scale",
        fields: [vec("vector", "Vector", [1, 2, 3]), num("scalar", "Scalar", "2")],
        result: "vector",
      },
    ],
  },

  // ===================== MATRICES =====================
  {
    id: "matrices",
    label: "Matrices",
    tagline: "Transformations, determinants & inverses",
    operations: [
      {
        id: "mat-add",
        label: "Add",
        blurb: "Element-wise sum of two matrices of equal shape.",
        endpoint: "/matrices/add",
        fields: [
          mat("matrix1", "Matrix A", [[1, 2], [3, 4]]),
          mat("matrix2", "Matrix B", [[5, 6], [7, 8]]),
        ],
        result: "matrix",
      },
      {
        id: "mat-sub",
        label: "Subtract",
        blurb: "Element-wise difference A − B.",
        endpoint: "/matrices/subtract",
        fields: [
          mat("matrix1", "Matrix A", [[5, 6], [7, 8]]),
          mat("matrix2", "Matrix B", [[1, 2], [3, 4]]),
        ],
        result: "matrix",
      },
      {
        id: "mat-mul",
        label: "Multiply (A × B)",
        blurb: "Matrix product. A's columns must match B's rows.",
        endpoint: "/matrices/multiply/matrix",
        fields: [
          mat("matrix1", "Matrix A", [[1, 2], [3, 4]]),
          mat("matrix2", "Matrix B", [[5, 6], [7, 8]]),
        ],
        result: "matrix",
      },
      {
        id: "mat-vec",
        label: "Matrix × vector",
        blurb: "Apply a matrix as a linear map to a vector.",
        endpoint: "/matrices/multiply/vector",
        fields: [
          mat("matrix", "Matrix", [[1, 2], [3, 4]]),
          vec("vector", "Vector", [1, 1]),
        ],
        result: "vector",
      },
      {
        id: "mat-scale",
        label: "Scale",
        blurb: "Multiply every entry by a scalar.",
        endpoint: "/matrices/scale",
        fields: [mat("matrix", "Matrix", [[1, 2], [3, 4]]), num("scalar", "Scalar", "2")],
        result: "matrix",
      },
      {
        id: "mat-det",
        label: "Determinant",
        blurb: "Signed volume scale factor of a square matrix.",
        endpoint: "/matrices/determinant",
        fields: [mat("matrix", "Matrix", [[1, 2], [3, 4]])],
        result: "scalar",
      },
      {
        id: "mat-inv",
        label: "Inverse",
        blurb: "Multiplicative inverse of a non-singular matrix.",
        endpoint: "/matrices/inverse",
        fields: [mat("matrix", "Matrix", [[4, 7], [2, 6]])],
        result: "matrix",
      },
      {
        id: "mat-transpose",
        label: "Transpose",
        blurb: "Reflect a matrix across its main diagonal.",
        endpoint: "/matrices/transpose",
        fields: [mat("matrix", "Matrix", [[1, 2, 3], [4, 5, 6]])],
        result: "matrix",
      },
    ],
  },

  // ===================== PRIMES =====================
  {
    id: "primes",
    label: "Primes",
    tagline: "Primality, sequences & factorisation",
    operations: [
      {
        id: "prime-check",
        label: "Is prime?",
        blurb: "Test a whole number greater than 1 for primality.",
        endpoint: "/primes/is_prime",
        fields: [int("number", "Number", "97")],
        result: "bool",
        resultLabel: "Primality",
      },
      {
        id: "prime-nth",
        label: "n-th prime",
        blurb: "Find the n-th prime number (1 → 2, 2 → 3, …).",
        endpoint: "/primes/nth_prime",
        fields: [int("n", "Index n", "25")],
        result: "scalar",
      },
      {
        id: "prime-list",
        label: "First n primes",
        blurb: "List the first n prime numbers.",
        endpoint: "/primes/list_primes",
        fields: [int("count", "How many", "20")],
        result: "intlist",
      },
      {
        id: "prime-fac",
        label: "Prime factorisation",
        blurb: "Decompose an integer into its prime factors.",
        endpoint: "/primes/factorization",
        fields: [int("number", "Number", "360")],
        result: "string",
      },
    ],
  },

  // ===================== GEOMETRY =====================
  {
    id: "geometry",
    label: "Geometry",
    tagline: "Area, perimeter, volume & surface area",
    operations: [
      // -- Area --
      {
        id: "geo-area-circle",
        label: "Area · Circle",
        blurb: "πr² for a circle of given radius.",
        endpoint: "/geometry/area/circle",
        fields: [num("radius", "Radius", "5")],
        result: "scalar",
      },
      {
        id: "geo-area-semicircle",
        label: "Area · Semicircle",
        blurb: "½πr² for a half-disc.",
        endpoint: "/geometry/area/semi_circle",
        fields: [num("radius", "Radius", "5")],
        result: "scalar",
      },
      {
        id: "geo-area-ellipse",
        label: "Area · Ellipse",
        blurb: "π·a·b for an ellipse.",
        endpoint: "/geometry/area/ellipse",
        fields: [num("semi_major", "Semi-major (a)", "5"), num("semi_minor", "Semi-minor (b)", "3")],
        result: "scalar",
      },
      {
        id: "geo-area-rect",
        label: "Area · Rectangle",
        blurb: "length × width.",
        endpoint: "/geometry/area/rectangle",
        fields: [num("length", "Length", "8"), num("width", "Width", "5")],
        result: "scalar",
      },
      {
        id: "geo-area-square",
        label: "Area · Square",
        blurb: "side².",
        endpoint: "/geometry/area/square",
        fields: [num("side", "Side", "6")],
        result: "scalar",
      },
      {
        id: "geo-area-parallelogram",
        label: "Area · Parallelogram",
        blurb: "a·b·sin θ with θ between the sides.",
        endpoint: "/geometry/area/parallelogram",
        fields: [num("side1", "Side a", "6"), num("side2", "Side b", "4"), num("theta", "Angle θ (deg)", "60")],
        result: "scalar",
      },
      {
        id: "geo-area-rhombus",
        label: "Area · Rhombus",
        blurb: "½·d₁·d₂ from the two diagonals.",
        endpoint: "/geometry/area/rhombus",
        fields: [num("diagonal1", "Diagonal d₁", "8"), num("diagonal2", "Diagonal d₂", "6")],
        result: "scalar",
      },
      {
        id: "geo-area-trapezoid",
        label: "Area · Trapezoid",
        blurb: "½·(b₁+b₂)·h.",
        endpoint: "/geometry/area/trapezoid",
        fields: [num("base1", "Base b₁", "8"), num("base2", "Base b₂", "5"), num("height", "Height", "4")],
        result: "scalar",
      },
      {
        id: "geo-area-polygon",
        label: "Area · Regular polygon",
        blurb: "Area of an n-sided regular polygon.",
        endpoint: "/geometry/area/polygon",
        fields: [int("sides", "Number of sides", "6"), num("side_length", "Side length", "4")],
        result: "scalar",
      },
      {
        id: "geo-area-tri-heron",
        label: "Area · Triangle (SSS)",
        blurb: "Heron's formula from three sides.",
        endpoint: "/geometry/area/triangle/heron",
        fields: [num("side1", "Side a", "3"), num("side2", "Side b", "4"), num("side3", "Side c", "5")],
        result: "scalar",
      },
      {
        id: "geo-area-tri-sas",
        label: "Area · Triangle (SAS)",
        blurb: "½·a·b·sin C from two sides & included angle.",
        endpoint: "/geometry/area/triangle/sas",
        fields: [num("side1", "Side a", "5"), num("side2", "Side b", "7"), num("angle", "Included angle (deg)", "45")],
        result: "scalar",
      },
      {
        id: "geo-area-tri-bh",
        label: "Area · Triangle (base·height)",
        blurb: "½·base·height.",
        endpoint: "/geometry/area/triangle/base_height",
        fields: [num("base", "Base", "6"), num("height", "Height", "4")],
        result: "scalar",
      },
      // -- Perimeter --
      {
        id: "geo-perim-circle",
        label: "Perimeter · Circle",
        blurb: "Circumference 2πr.",
        endpoint: "/geometry/perimeter/circle",
        fields: [num("radius", "Radius", "5")],
        result: "scalar",
      },
      {
        id: "geo-perim-rect",
        label: "Perimeter · Rectangle",
        blurb: "2·(length + width).",
        endpoint: "/geometry/perimeter/rectangle",
        fields: [num("length", "Length", "8"), num("width", "Width", "5")],
        result: "scalar",
      },
      {
        id: "geo-perim-square",
        label: "Perimeter · Square",
        blurb: "4·side.",
        endpoint: "/geometry/perimeter/square",
        fields: [num("side", "Side", "6")],
        result: "scalar",
      },
      {
        id: "geo-perim-polygon",
        label: "Perimeter · Regular polygon",
        blurb: "n·side.",
        endpoint: "/geometry/perimeter/polygon",
        fields: [int("sides", "Number of sides", "6"), num("side_length", "Side length", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-triangle",
        label: "Perimeter · Triangle",
        blurb: "Sum of the three sides.",
        endpoint: "/geometry/perimeter/triangle",
        fields: [num("side1", "Side a", "3"), num("side2", "Side b", "4"), num("side3", "Side c", "5")],
        result: "scalar",
      },
      {
        id: "geo-perim-trapezoid",
        label: "Perimeter · Trapezoid",
        blurb: "Sum of the two bases and the two legs.",
        endpoint: "/geometry/perimeter/trapezoid",
        fields: [
          num("base1", "Base b₁", "8"),
          num("base2", "Base b₂", "5"),
          num("leg1", "Leg 1", "4.5"),
          num("leg2", "Leg 2", "5"),
        ],
        result: "scalar",
      },
      {
        id: "geo-perim-pentagon",
        label: "Perimeter · Pentagon",
        blurb: "5·side (regular pentagon).",
        endpoint: "/geometry/perimeter/pentagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-hexagon",
        label: "Perimeter · Hexagon",
        blurb: "6·side (regular hexagon).",
        endpoint: "/geometry/perimeter/hexagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-heptagon",
        label: "Perimeter · Heptagon",
        blurb: "7·side (regular heptagon).",
        endpoint: "/geometry/perimeter/heptagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-octagon",
        label: "Perimeter · Octagon",
        blurb: "8·side (regular octagon).",
        endpoint: "/geometry/perimeter/octagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-nonagon",
        label: "Perimeter · Nonagon",
        blurb: "9·side (regular nonagon).",
        endpoint: "/geometry/perimeter/nonagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-perim-decagon",
        label: "Perimeter · Decagon",
        blurb: "10·side (regular decagon).",
        endpoint: "/geometry/perimeter/decagon",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      // -- Volume --
      {
        id: "geo-vol-cube",
        label: "Volume · Cube",
        blurb: "side³.",
        endpoint: "/geometry/volume/cube",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-vol-rect-prism",
        label: "Volume · Rectangular prism",
        blurb: "length × width × height.",
        endpoint: "/geometry/volume/rectangular_prism",
        fields: [num("length", "Length", "5"), num("width", "Width", "4"), num("height", "Height", "3")],
        result: "scalar",
      },
      {
        id: "geo-vol-cylinder",
        label: "Volume · Cylinder",
        blurb: "πr²h.",
        endpoint: "/geometry/volume/cylinder",
        fields: [num("radius", "Radius", "3"), num("height", "Height", "7")],
        result: "scalar",
      },
      {
        id: "geo-vol-cone",
        label: "Volume · Cone",
        blurb: "⅓πr²h.",
        endpoint: "/geometry/volume/cone",
        fields: [num("radius", "Radius", "3"), num("height", "Height", "7")],
        result: "scalar",
      },
      {
        id: "geo-vol-sphere",
        label: "Volume · Sphere",
        blurb: "4⁄3·πr³.",
        endpoint: "/geometry/volume/sphere",
        fields: [num("radius", "Radius", "5")],
        result: "scalar",
      },
      {
        id: "geo-vol-tetra",
        label: "Volume · Tetrahedron",
        blurb: "Regular tetrahedron from edge length.",
        endpoint: "/geometry/volume/tetrahedron",
        fields: [num("side", "Edge", "4")],
        result: "scalar",
      },
      {
        id: "geo-vol-octa",
        label: "Volume · Octahedron",
        blurb: "Regular octahedron from edge length.",
        endpoint: "/geometry/volume/octahedron",
        fields: [num("side", "Edge", "3")],
        result: "scalar",
      },
      {
        id: "geo-vol-dodeca",
        label: "Volume · Dodecahedron",
        blurb: "Regular dodecahedron from edge length.",
        endpoint: "/geometry/volume/dodecahedron",
        fields: [num("side", "Edge", "2")],
        result: "scalar",
      },
      {
        id: "geo-vol-ellipsoid",
        label: "Volume · Ellipsoid",
        blurb: "4⁄3·π·a·b·c from three semi-axes.",
        endpoint: "/geometry/volume/ellipsoid",
        fields: [
          num("semi_major", "Semi-axis a", "5"),
          num("semi_minor", "Semi-axis b", "3"),
          num("axis3", "Semi-axis c", "2"),
        ],
        result: "scalar",
      },
      {
        id: "geo-vol-prism",
        label: "Volume · Prism",
        blurb: "base area × height.",
        endpoint: "/geometry/volume/prism",
        fields: [num("base_area", "Base area", "16"), num("height", "Height", "10")],
        result: "scalar",
      },
      {
        id: "geo-vol-icosa",
        label: "Volume · Icosahedron",
        blurb: "Regular icosahedron from edge length.",
        endpoint: "/geometry/volume/icosahedron",
        fields: [num("side", "Edge", "2")],
        result: "scalar",
      },
      // -- Surface area --
      {
        id: "geo-sa-cube",
        label: "Surface area · Cube",
        blurb: "6·side².",
        endpoint: "/geometry/surface_area/cube",
        fields: [num("side", "Side", "4")],
        result: "scalar",
      },
      {
        id: "geo-sa-sphere",
        label: "Surface area · Sphere",
        blurb: "4πr².",
        endpoint: "/geometry/surface_area/sphere",
        fields: [num("radius", "Radius", "5")],
        result: "scalar",
      },
      {
        id: "geo-sa-cylinder",
        label: "Surface area · Cylinder",
        blurb: "2πr·(r + h).",
        endpoint: "/geometry/surface_area/cylinder",
        fields: [num("radius", "Radius", "3"), num("height", "Height", "7")],
        result: "scalar",
      },
      {
        id: "geo-sa-cone",
        label: "Surface area · Cone",
        blurb: "πr·(r + slant).",
        endpoint: "/geometry/surface_area/cone",
        fields: [num("radius", "Radius", "3"), num("height", "Height", "7")],
        result: "scalar",
      },
      {
        id: "geo-sa-rect-prism",
        label: "Surface area · Rectangular prism",
        blurb: "2·(lw + lh + wh).",
        endpoint: "/geometry/surface_area/rectangular_prism",
        fields: [num("length", "Length", "5"), num("width", "Width", "4"), num("height", "Height", "3")],
        result: "scalar",
      },
      {
        id: "geo-sa-ellipsoid",
        label: "Surface area · Ellipsoid",
        blurb: "Thomsen approximation from three semi-axes.",
        endpoint: "/geometry/surface_area/ellipsoid",
        fields: [
          num("semi_major", "Semi-axis a", "5"),
          num("semi_minor", "Semi-axis b", "3"),
          num("axis3", "Semi-axis c", "2"),
        ],
        result: "scalar",
      },
      {
        id: "geo-sa-prism",
        label: "Surface area · Prism",
        blurb: "2·base area + base perimeter × height.",
        endpoint: "/geometry/surface_area/prism",
        fields: [
          num("base_area", "Base area", "16"),
          num("base_perimeter", "Base perimeter", "16"),
          num("height", "Height", "10"),
        ],
        result: "scalar",
      },
      {
        id: "geo-sa-tetra",
        label: "Surface area · Tetrahedron",
        blurb: "√3·side².",
        endpoint: "/geometry/surface_area/tetrahedron",
        fields: [num("side", "Edge", "4")],
        result: "scalar",
      },
      {
        id: "geo-sa-octa",
        label: "Surface area · Octahedron",
        blurb: "2·√3·side².",
        endpoint: "/geometry/surface_area/octahedron",
        fields: [num("side", "Edge", "3")],
        result: "scalar",
      },
      {
        id: "geo-sa-dodeca",
        label: "Surface area · Dodecahedron",
        blurb: "3·√(25 + 10√5)·side².",
        endpoint: "/geometry/surface_area/dodecahedron",
        fields: [num("side", "Edge", "2")],
        result: "scalar",
      },
      {
        id: "geo-sa-icosa",
        label: "Surface area · Icosahedron",
        blurb: "5·√3·side².",
        endpoint: "/geometry/surface_area/icosahedron",
        fields: [num("side", "Edge", "2")],
        result: "scalar",
      },
    ],
  },

  // ===================== TRIANGLE SOLVER =====================
  {
    id: "triangles",
    label: "Triangle solver",
    tagline: "Solve any triangle from 3 knowns",
    operations: [
      {
        id: "tri-solve",
        label: "Solve triangle",
        blurb:
          "Provide any three values including at least one side (sides a, b, c; angles A, B, C in degrees). Leave the rest blank.",
        endpoint: "/triangles/solve",
        fields: [
          num("a", "Side a", "3", "Opposite angle A"),
          num("b", "Side b", "4", "Opposite angle B"),
          { ...num("c", "Side c", ""), optional: true },
          { ...num("A", "Angle A (deg)", ""), optional: true },
          { ...num("B", "Angle B (deg)", ""), optional: true },
          { ...num("C", "Angle C (deg)", "90"), optional: true },
        ].map((f) => ({ ...f, optional: true })),
        result: "triangle",
      },
    ],
  },

  // ===================== HIGH PRECISION =====================
  {
    id: "irrationals",
    label: "High precision",
    tagline: "Arbitrary-precision arithmetic & trig",
    operations: [
      {
        id: "hp-add",
        label: "Add",
        blurb: "Sum two numbers to arbitrary precision.",
        endpoint: "/irrationals/add",
        fields: [txt("operand1", "Operand A", "1"), txt("operand2", "Operand B", "3")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-sub",
        label: "Subtract",
        blurb: "A − B to arbitrary precision.",
        endpoint: "/irrationals/subtract",
        fields: [txt("operand1", "Operand A", "10"), txt("operand2", "Operand B", "3")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-mul",
        label: "Multiply",
        blurb: "A × B to arbitrary precision.",
        endpoint: "/irrationals/multiply",
        fields: [txt("operand1", "Operand A", "1.5"), txt("operand2", "Operand B", "7")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-div",
        label: "Divide",
        blurb: "A ÷ B to arbitrary precision.",
        endpoint: "/irrationals/divide",
        fields: [txt("operand1", "Operand A", "1"), txt("operand2", "Operand B", "7")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-pow",
        label: "Power",
        blurb: "A raised to an integer exponent B.",
        endpoint: "/irrationals/power",
        fields: [txt("operand1", "Base A", "2"), txt("operand2", "Exponent B (integer)", "64")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-sqrt",
        label: "Square root",
        blurb: "√A to arbitrary precision.",
        endpoint: "/irrationals/sqrt",
        fields: [txt("operand", "Operand", "2")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-pi",
        label: "π",
        blurb: "Compute π to arbitrary precision.",
        endpoint: "/irrationals/pi",
        method: "GET",
        fields: [],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-e",
        label: "e",
        blurb: "Compute Euler's number e to arbitrary precision.",
        endpoint: "/irrationals/e",
        method: "GET",
        fields: [],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-sin",
        label: "sin",
        blurb: "Sine of an angle.",
        endpoint: "/irrationals/sin",
        fields: [
          txt("angle", "Angle", "1"),
          { name: "radians", label: "Angle in radians", type: "bool", initial: true } as Field,
        ],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-cos",
        label: "cos",
        blurb: "Cosine of an angle.",
        endpoint: "/irrationals/cos",
        fields: [
          txt("angle", "Angle", "1"),
          { name: "radians", label: "Angle in radians", type: "bool", initial: true } as Field,
        ],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-tan",
        label: "tan",
        blurb: "Tangent of an angle.",
        endpoint: "/irrationals/tan",
        fields: [
          txt("angle", "Angle", "1"),
          { name: "radians", label: "Angle in radians", type: "bool", initial: true } as Field,
        ],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-arcsin",
        label: "arcsin",
        blurb: "Inverse sine (result in radians).",
        endpoint: "/irrationals/arcsin",
        fields: [txt("operand", "Operand (−1 … 1)", "0.5")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-arccos",
        label: "arccos",
        blurb: "Inverse cosine (result in radians).",
        endpoint: "/irrationals/arccos",
        fields: [txt("operand", "Operand (−1 … 1)", "0.5")],
        query: [PRECISION],
        result: "string",
      },
      {
        id: "hp-arctan",
        label: "arctan",
        blurb: "Inverse tangent (result in radians).",
        endpoint: "/irrationals/arctan",
        fields: [txt("operand", "Operand", "1")],
        query: [PRECISION],
        result: "string",
      },
    ],
  },

  // ===================== CAS =====================
  {
    id: "cas",
    label: "Algebra (CAS)",
    tagline: "Symbolic algebra & calculus",
    operations: [
      {
        id: "cas-simplify",
        label: "Simplify",
        blurb: "Simplify an algebraic expression.",
        endpoint: "/cas/simplify",
        fields: [txt("expression", "Expression", "(x**2 - 1)/(x - 1)")],
        result: "string",
      },
      {
        id: "cas-expand",
        label: "Expand",
        blurb: "Expand products and powers.",
        endpoint: "/cas/expand",
        fields: [txt("expression", "Expression", "(x + 2)**3")],
        result: "string",
      },
      {
        id: "cas-factor",
        label: "Factor",
        blurb: "Factor an expression over the rationals.",
        endpoint: "/cas/factor",
        fields: [txt("expression", "Expression", "x**2 - 5*x + 6")],
        result: "string",
      },
      {
        id: "cas-diff",
        label: "Differentiate",
        blurb: "Derivative with respect to the free variable.",
        endpoint: "/cas/differentiate",
        fields: [txt("expression", "Expression", "sin(x)*x**2")],
        result: "string",
      },
      {
        id: "cas-int",
        label: "Integrate",
        blurb: "Indefinite integral with respect to a variable.",
        endpoint: "/cas/integrate",
        fields: [txt("expression", "Expression", "x**2"), txt("variable", "Variable", "x")],
        result: "string",
      },
      {
        id: "cas-defint",
        label: "Definite integral",
        blurb: "Integrate over [lower, upper].",
        endpoint: "/cas/definite-integral",
        fields: [
          txt("expression", "Expression", "x**2"),
          txt("variable", "Variable", "x"),
          txt("lower_limit", "Lower limit", "0"),
          txt("upper_limit", "Upper limit", "1"),
        ],
        result: "string",
      },
      {
        id: "cas-solve",
        label: "Solve equation",
        blurb: "Solve a single-variable equation (use '=').",
        endpoint: "/cas/solve-equation",
        fields: [txt("equation", "Equation", "x**2 - 4 = 0"), txt("variable", "Variable", "x")],
        result: "string",
      },
      {
        id: "cas-solve-multi",
        label: "Solve system",
        blurb: "Solve simultaneous equations (one per line).",
        endpoint: "/cas/solve-multivariable",
        fields: [
          {
            name: "equations",
            label: "Equations (one per line)",
            type: "textlist",
            initial: ["x + y = 10", "x - y = 2"],
          },
          txt("variables", "Variables (comma-separated)", "x, y"),
        ],
        result: "string",
      },
      {
        id: "cas-solve-diff",
        label: "Differential equation",
        blurb: "Solve a first-order ODE in y(x). Use y' for the derivative and include '='.",
        endpoint: "/cas/solve-differential",
        fields: [txt("equation", "Equation", "y' + y = 0")],
        result: "string",
      },
    ],
  },

  // ===================== MULTIVARIABLE CALCULUS =====================
  {
    id: "calculus",
    label: "Calculus",
    tagline: "Vector & multivariable calculus",
    operations: [
      {
        id: "calc-partial",
        label: "Partial derivative",
        blurb: "∂/∂x of a multivariable expression, to any order.",
        endpoint: "/calculus/partial",
        fields: [
          txt("expression", "Expression f", "x**2*y + sin(x*y)"),
          txt("variable", "Variable", "x"),
          int("order", "Order", "1"),
        ],
        result: "string",
      },
      {
        id: "calc-gradient",
        label: "Gradient (∇f)",
        blurb: "Vector of first partials of a scalar field.",
        endpoint: "/calculus/gradient",
        fields: [
          txt("expression", "Scalar field f", "x**2 + y**2 + z**2"),
          txt("variables", "Variables", "x, y, z"),
        ],
        result: "exprvector",
      },
      {
        id: "calc-divergence",
        label: "Divergence (∇·F)",
        blurb: "Divergence of a vector field (one component per line).",
        endpoint: "/calculus/divergence",
        fields: [
          tlist("field", "Vector field F", ["x*y", "y*z", "z*x"], "One component per line, matching the variables."),
          txt("variables", "Variables", "x, y, z"),
        ],
        result: "string",
      },
      {
        id: "calc-curl",
        label: "Curl (∇×F)",
        blurb: "Curl of a 3-D vector field.",
        endpoint: "/calculus/curl",
        fields: [
          tlist("field", "Vector field F", ["x*y", "y*z", "z*x"], "Exactly three components."),
          txt("variables", "Variables", "x, y, z"),
        ],
        result: "exprvector",
      },
      {
        id: "calc-laplacian",
        label: "Laplacian (∇²f)",
        blurb: "Sum of unmixed second partials.",
        endpoint: "/calculus/laplacian",
        fields: [
          txt("expression", "Scalar field f", "x**2 + y**2 + z**2"),
          txt("variables", "Variables", "x, y, z"),
        ],
        result: "string",
      },
      {
        id: "calc-hessian",
        label: "Hessian",
        blurb: "Matrix of second partial derivatives.",
        endpoint: "/calculus/hessian",
        fields: [
          txt("expression", "Scalar field f", "x**2*y + y**3"),
          txt("variables", "Variables", "x, y"),
        ],
        result: "exprmatrix",
      },
      {
        id: "calc-jacobian",
        label: "Jacobian",
        blurb: "Jacobian matrix of a vector-valued function.",
        endpoint: "/calculus/jacobian",
        fields: [
          tlist("functions", "Component functions", ["x*y", "x + y"], "One function per line."),
          txt("variables", "Variables", "x, y"),
        ],
        result: "exprmatrix",
      },
      {
        id: "calc-dirderiv",
        label: "Directional derivative",
        blurb: "Rate of change of f along a direction (auto-normalised).",
        endpoint: "/calculus/directional-derivative",
        fields: [
          txt("expression", "Scalar field f", "x**2 + y**2"),
          txt("variables", "Variables", "x, y"),
          tlist("direction", "Direction vector", ["1", "1"], "One component per line, matching the variables."),
        ],
        result: "string",
      },
      {
        id: "calc-double-int",
        label: "Double integral",
        blurb: "Iterated ∫∫ — inner variable integrated first.",
        endpoint: "/calculus/double-integral",
        fields: [
          txt("expression", "Integrand", "x*y"),
          txt("var1", "Inner variable", "x"),
          txt("lower1", "Inner lower", "0"),
          txt("upper1", "Inner upper", "1"),
          txt("var2", "Outer variable", "y"),
          txt("lower2", "Outer lower", "0"),
          txt("upper2", "Outer upper", "2"),
        ],
        result: "string",
      },
      {
        id: "calc-triple-int",
        label: "Triple integral",
        blurb: "Iterated ∫∫∫ — innermost variable integrated first.",
        endpoint: "/calculus/triple-integral",
        fields: [
          txt("expression", "Integrand", "1"),
          txt("var1", "Innermost variable", "x"),
          txt("lower1", "Lower", "0"),
          txt("upper1", "Upper", "1"),
          txt("var2", "Middle variable", "y"),
          txt("lower2", "Lower", "0"),
          txt("upper2", "Upper", "1"),
          txt("var3", "Outermost variable", "z"),
          txt("lower3", "Lower", "0"),
          txt("upper3", "Upper", "1"),
        ],
        result: "string",
      },
      {
        id: "calc-limit",
        label: "Limit",
        blurb: "Limit as a variable approaches a point (use 'oo' for ∞).",
        endpoint: "/calculus/limit",
        fields: [
          txt("expression", "Expression", "sin(x)/x"),
          txt("variable", "Variable", "x"),
          txt("point", "Approaching", "0"),
          txt("direction", "Direction (+, - or +-)", "+"),
        ],
        result: "string",
      },
      {
        id: "calc-taylor",
        label: "Taylor series",
        blurb: "Series expansion about a point, to a given order.",
        endpoint: "/calculus/taylor-series",
        fields: [
          txt("expression", "Expression", "exp(x)"),
          txt("variable", "Variable", "x"),
          txt("point", "About point", "0"),
          int("order", "Order", "6"),
        ],
        result: "string",
      },
    ],
  },

  // ===================== PYTHAGOREAN =====================
  {
    id: "pythagorean",
    label: "Pythagorean",
    tagline: "Generate right-triangle triples",
    operations: [
      {
        id: "pyth-gen",
        label: "Generate triples",
        blurb: "All Pythagorean triples (a,b,c) up to a maximum hypotenuse.",
        endpoint: "/pythagorean/generate",
        fields: [int("max_hypotenuse", "Max hypotenuse", "50")],
        query: [
          {
            name: "primitive",
            label: "Primitive only",
            type: "bool",
            initial: false,
            help: "Only triples with gcd(a,b,c) = 1.",
          },
        ],
        result: "triples",
      },
    ],
  },

  // ===================== STATISTICS =====================
  {
    id: "statistics",
    label: "Statistics",
    tagline: "Descriptive stats on a data set",
    operations: [
      {
        id: "stat-summary",
        label: "Summary",
        blurb:
          "Full descriptive summary of a data set — count, mean, median, mode, quartiles, variance, standard deviation, skewness and more.",
        endpoint: "/statistics/summary",
        fields: [vec("data", "Data set", [4, 8, 15, 16, 23, 42])],
        result: "table",
        resultLabel: "Summary",
      },
      {
        id: "stat-mean",
        label: "Mean",
        blurb: "Arithmetic mean (average) of the values.",
        endpoint: "/statistics/mean",
        fields: [vec("data", "Data set", [4, 8, 15, 16, 23, 42])],
        result: "scalar",
        resultLabel: "Mean",
      },
      {
        id: "stat-median",
        label: "Median",
        blurb: "Middle value once the data set is sorted.",
        endpoint: "/statistics/median",
        fields: [vec("data", "Data set", [4, 8, 15, 16, 23, 42])],
        result: "scalar",
        resultLabel: "Median",
      },
      {
        id: "stat-mode",
        label: "Mode",
        blurb: "Most frequent value(s) in the data set.",
        endpoint: "/statistics/mode",
        fields: [vec("data", "Data set", [2, 4, 4, 5, 7, 7, 9])],
        result: "vector",
        resultLabel: "Mode",
      },
      {
        id: "stat-variance",
        label: "Variance",
        blurb: "Average squared deviation from the mean.",
        endpoint: "/statistics/variance",
        fields: [
          vec("data", "Data set", [4, 8, 15, 16, 23, 42]),
          {
            name: "sample",
            label: "Sample (n − 1)",
            type: "bool",
            initial: true,
          } as Field,
        ],
        result: "scalar",
        resultLabel: "Variance",
      },
      {
        id: "stat-stddev",
        label: "Standard deviation",
        blurb: "Spread of the data about the mean.",
        endpoint: "/statistics/standard-deviation",
        fields: [
          vec("data", "Data set", [4, 8, 15, 16, 23, 42]),
          {
            name: "sample",
            label: "Sample (n − 1)",
            type: "bool",
            initial: true,
          } as Field,
        ],
        result: "scalar",
        resultLabel: "Std deviation",
      },
    ],
  },

  // ===================== NUMBER BASES =====================
  {
    id: "bases",
    label: "Number bases",
    tagline: "Convert between binary, decimal & hex",
    operations: [
      {
        id: "base-convert",
        label: "Convert base",
        blurb:
          "Read a number written in any base from 2 to 36 and show it in decimal, binary, octal and hexadecimal.",
        endpoint: "/bases/convert",
        fields: [
          txt("number", "Number", "2A"),
          int("from_base", "Source base", "16", "The base the number above is written in (2–36)."),
        ],
        result: "table",
        resultLabel: "Conversions",
      },
    ],
  },
];

export const ALL_OPERATIONS: Operation[] = CATEGORIES.flatMap((c) => c.operations);
