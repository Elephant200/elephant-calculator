// Schematic SVG diagrams for geometry operations. The shape is inferred from
// the operation's endpoint (e.g. "/geometry/area/circle" → "circle"), so no
// per-operation wiring is needed. Returns null when there's no diagram.

type Props = { endpoint: string };

// Map an endpoint to a diagram key. Triangles have sub-paths
// (/area/triangle/heron); everything else keys off the final segment.
function shapeKey(endpoint: string): string | null {
  const m = endpoint.match(/^\/geometry\/(?:area|perimeter|volume|surface_area)\/(.+)$/);
  if (!m) return null;
  const rest = m[1];
  if (rest.startsWith("triangle")) return "triangle";
  return rest; // circle, semi_circle, rectangle, rectangular_prism, …
}

const ACCENT = "var(--accent)";
const FILL = "color-mix(in srgb, var(--accent) 9%, transparent)";
const MUTED = "var(--muted)";

function L(x: number, y: number, text: string) {
  return (
    <text
      x={x}
      y={y}
      fill={MUTED}
      fontSize="12"
      fontFamily="var(--font-mono), monospace"
      textAnchor="middle"
      dominantBaseline="middle"
    >
      {text}
    </text>
  );
}

// Each entry draws into a 220×150 viewBox.
const SHAPES: Record<string, React.ReactNode> = {
  circle: (
    <>
      <circle cx="110" cy="75" r="55" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <line x1="110" y1="75" x2="165" y2="75" stroke={ACCENT} strokeWidth="1.5" strokeDasharray="4 3" />
      <circle cx="110" cy="75" r="2.5" fill={ACCENT} />
      {L(138, 63, "r")}
    </>
  ),
  semi_circle: (
    <>
      <path d="M45 100 A65 65 0 0 1 175 100 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <line x1="110" y1="100" x2="175" y2="100" stroke={ACCENT} strokeWidth="1.5" strokeDasharray="4 3" />
      {L(143, 113, "r")}
    </>
  ),
  ellipse: (
    <>
      <ellipse cx="110" cy="75" rx="75" ry="42" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <line x1="110" y1="75" x2="185" y2="75" stroke={ACCENT} strokeWidth="1.5" strokeDasharray="4 3" />
      <line x1="110" y1="75" x2="110" y2="33" stroke={ACCENT} strokeWidth="1.5" strokeDasharray="4 3" />
      {L(150, 64, "a")}
      {L(98, 52, "b")}
    </>
  ),
  square: (
    <>
      <rect x="65" y="30" width="90" height="90" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      {L(110, 134, "s")}
    </>
  ),
  rectangle: (
    <>
      <rect x="40" y="42" width="140" height="66" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      {L(110, 122, "length")}
      {L(28, 75, "w")}
    </>
  ),
  parallelogram: (
    <>
      <path d="M55 115 L95 40 L185 40 L145 115 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      {L(125, 128, "a")}
      {L(60, 78, "b")}
    </>
  ),
  rhombus: (
    <>
      <path d="M110 25 L175 75 L110 125 L45 75 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <line x1="45" y1="75" x2="175" y2="75" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      <line x1="110" y1="25" x2="110" y2="125" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      {L(150, 64, "d₁")}
      {L(96, 100, "d₂")}
    </>
  ),
  trapezoid: (
    <>
      <path d="M40 115 L185 115 L150 40 L75 40 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      {L(112, 128, "b₁")}
      {L(112, 30, "b₂")}
    </>
  ),
  polygon: (
    <>
      <path
        d="M110 22 L162 52 L162 112 L110 142 L58 112 L58 52 Z"
        fill={FILL}
        stroke={ACCENT}
        strokeWidth="2"
      />
      {L(190, 82, "n sides")}
    </>
  ),
  triangle: (
    <>
      <path d="M40 120 L180 120 L120 35 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      {L(110, 133, "a")}
      {L(160, 80, "b")}
      {L(70, 75, "c")}
    </>
  ),
  // --- 3-D solids (isometric-ish line art) ---
  cube: (
    <>
      <path d="M60 55 L120 55 L120 120 L60 120 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M60 55 L90 30 L150 30 L120 55" fill="none" stroke={ACCENT} strokeWidth="2" />
      <path d="M120 55 L150 30 L150 95 L120 120" fill="none" stroke={ACCENT} strokeWidth="2" />
      <line x1="60" y1="120" x2="90" y2="95" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      <line x1="90" y1="95" x2="150" y2="95" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      <line x1="90" y1="95" x2="90" y2="30" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      {L(135, 138, "s")}
    </>
  ),
  rectangular_prism: (
    <>
      <path d="M45 60 L135 60 L135 120 L45 120 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M45 60 L75 35 L165 35 L135 60" fill="none" stroke={ACCENT} strokeWidth="2" />
      <path d="M135 60 L165 35 L165 95 L135 120" fill="none" stroke={ACCENT} strokeWidth="2" />
      {L(90, 134, "l")}
      {L(33, 90, "w")}
      {L(155, 80, "h")}
    </>
  ),
  cylinder: (
    <>
      <ellipse cx="110" cy="40" rx="50" ry="16" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M60 40 L60 110" stroke={ACCENT} strokeWidth="2" />
      <path d="M160 40 L160 110" stroke={ACCENT} strokeWidth="2" />
      <path d="M60 110 A50 16 0 0 0 160 110" fill="none" stroke={ACCENT} strokeWidth="2" />
      <line x1="110" y1="40" x2="160" y2="40" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      {L(135, 30, "r")}
      {L(175, 78, "h")}
    </>
  ),
  cone: (
    <>
      <path d="M110 25 L160 110 L60 110 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M60 110 A50 14 0 0 0 160 110" fill="none" stroke={ACCENT} strokeWidth="2" />
      <path d="M60 110 A50 14 0 0 1 160 110" fill="none" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      <line x1="110" y1="110" x2="160" y2="110" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      <line x1="110" y1="25" x2="110" y2="110" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      {L(135, 122, "r")}
      {L(122, 70, "h")}
    </>
  ),
  sphere: (
    <>
      <circle cx="110" cy="75" r="52" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <ellipse cx="110" cy="75" rx="52" ry="17" fill="none" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      <line x1="110" y1="75" x2="162" y2="75" stroke={ACCENT} strokeWidth="1.5" strokeDasharray="4 3" />
      {L(136, 63, "r")}
    </>
  ),
  ellipsoid: (
    <>
      <ellipse cx="110" cy="75" rx="72" ry="40" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <ellipse cx="110" cy="75" rx="72" ry="14" fill="none" stroke={ACCENT} strokeWidth="1" strokeDasharray="3 3" />
      <line x1="110" y1="75" x2="182" y2="75" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      <line x1="110" y1="75" x2="110" y2="35" stroke={ACCENT} strokeWidth="1.3" strokeDasharray="4 3" />
      {L(150, 64, "a")}
      {L(98, 52, "b")}
    </>
  ),
  prism: (
    <>
      <path d="M50 60 L110 60 L110 120 L50 120 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M50 60 L85 35 L145 35 L110 60" fill="none" stroke={ACCENT} strokeWidth="2" />
      <path d="M110 60 L145 35 L145 95 L110 120" fill="none" stroke={ACCENT} strokeWidth="2" />
      {L(170, 78, "h")}
    </>
  ),
  // Platonic solids share a faceted icon; the selector names the specific solid.
  polyhedron: (
    <>
      <path d="M110 20 L175 65 L150 130 L70 130 L45 65 Z" fill={FILL} stroke={ACCENT} strokeWidth="2" />
      <path d="M110 20 L110 80 M45 65 L110 80 L175 65 M70 130 L110 80 L150 130" fill="none" stroke={ACCENT} strokeWidth="1.3" />
      {L(110, 145, "edge s")}
    </>
  ),
};

export function hasGeometryDiagram(endpoint: string): boolean {
  const key = shapeKey(endpoint);
  return key != null && key in SHAPES;
}

export function GeometryDiagram({ endpoint }: Props) {
  const key = shapeKey(endpoint);
  const art = key ? SHAPES[key] : null;
  if (!art) return null;

  return (
    <div className="panel-quiet flex items-center justify-center p-3" aria-hidden>
      <svg
        viewBox="0 0 220 150"
        className="h-[150px] w-full max-w-[280px]"
        role="img"
      >
        {art}
      </svg>
    </div>
  );
}
