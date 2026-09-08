# Orange Plan Academy — visual style block

Paste this at the top of every visual prompt. It is the app's real design
system, pulled from `src/styles/redesign-tokens.css` and
`ORANGE_PLAN_DATA_PALETTE.md`, so course graphics match what students see
in the product.

---

## STYLE BLOCK (paste verbatim)

Design a clean, flat, editorial explainer graphic for a financial-planning
course. 16:9, safe margins, no drop shadows, no gradients on data, no 3D,
no stock-photo imagery, no icons-for-decoration. Generous whitespace.
Everything must read at 1080p on a phone.

Palette (use these exact hexes):
- Page background #FAF6EF · surface #FFFDF9 · recessed #F2EDE2
- Ink #2C2A26 · secondary ink #8A8276 · hairlines #EDE6D8
- Bitcoin #DD7E52 (tint #E8A87E, soft #FDF1EB)
- Stocks #7491CB · Bonds #7697A4 · Cash #BAB1A0 · Real estate #34A07E
- Taxable #EAC258 · Tax-deferred #9088B8 · Roth #3DA68F
- Income floor #55A184 · Spending #8B93A1 · Debt payments #64748B
- Borrowed cash (BTC-backed loan) #6B4E9E
- Taxes #B85C50 · Risk / shortfall #C76A6A
- Good #1D9E75 · Warning #F3A31A
- Reference and target lines: #2C2A26, thin, dashed, never a data color

Hard rules:
1. Orange means Bitcoin and nothing else. Never use it for a generic accent.
2. Collateralized or locked Bitcoin uses the Bitcoin tint, because it is
   still Bitcoin. Borrowed cash against it uses the loan purple.
3. Reference lines (spending need, target, threshold) are neutral, not a
   data series.
4. No gradients or patterns on data. Area fills may use one series color
   with a vertical alpha fade.
5. Type: one clean humanist sans. Labels sentence case. Numbers in digits.
6. Say "Bitcoin," never "crypto."
7. No dollar figures that imply a promise. Illustrative numbers only.
8. Never render a law-set figure (bracket, limit, exemption, RMD age) as
   a fixed number in artwork; those go on screen from the app instead.

## MOTION (when animating)

- Reveal in the order the narration says it. One element at a time.
- Ease-out, 300-500ms per element, 200ms stagger.
- Hold the finished frame at least 3 seconds; it has to survive a pause.
- Animate the thing that changes, nothing else. No idle drift, no parallax.
- Anything crossing a threshold moves toward the line, then the line
  flashes once at the crossing.
