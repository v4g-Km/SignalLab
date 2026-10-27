# SignalLab — From Textbook to Signal Data-Flow

Reverse-engineering a mechanical-engineering testing textbook
(*《机械工程测试技术基础》(Fundamentals of Measurement Techniques for Mechanical Engineering)*) into the core route of signal data-flow —
one minimal Python MVP per chapter, grounded in how the human brain
actually learns.


## What this is

This is **not** a tutorial dump, and **not** run-and-forget code.
It is a learning artifact that:

- extracts **one core causal chain** (the "signal data-flow") from the
  textbook, instead of following the book's chapter order;
- pairs every concept with a **minimal runnable Python MVP** so you can
  *see* the physics, not just read it;
- grounds the whole process in **cognitive-science principles of
  learning** (the seven principles below);
- connects abstract math/physics back to **real engineering** — in my
  case, a brain–computer-interface chess system.

## The learning principles

> *Note:These principles are not textbook doctrine. They were synthesized by prompting an AI against my long-term learning journals and the recursive questioning patterns I developed while studying.*

1. **Knowledge as a Pipeline**: Understand concepts as continuous transformations, not isolated checklists.
2. **Explicit Handoffs**: Trace and define the interface (`input -> transformation -> output`) at every boundary.
3. **Phenomenology First**: Follow the sequence of `Phenomenon -> Intuition -> Mathematical Formulation`. Formal math serves as the *refinement* of physical intuition, not its entry point.
4. **Scaffolding Integrity**: Patch and consolidate existing mental models before layering on new abstractions.
5. **Trade-offs Over Definitions**: Articulate design constraints and engineering compromises, not merely textbook definitions.
6. **Mechanistic Grounding**: Every abstraction and metaphor must collapse cleanly back to a physical mechanism.
7. **Isomorphic Mapping**: Anchor every new insight with an isomorphic bridge to systems you already command.

## How it's built

1. Textbook PDF → OCR → Markdown.
2. Reinforce each chapter's understanding with the help of an AI.
3. Write one minimal MVP script per concept; the AI helps refine it.
4. **Re-type / re-derive each station by hand, then commit it.**

## The signal data-flow route

| Stage | Theme | Core question | Script |
|---|---|---|---|
| 0 | The map | Why is your system already a test system? | — |
| 1 | Time domain | What does this signal look like? | `s01` |
| 2 | Frequency domain | What frequencies compose it? | `s02`, `s02b` |
| 3 | Sampling | How do we capture a continuous signal? | `s03` |
| 4 | Filtering | How do we clean the noise? | `s04` |
| 5 | Sensors | How is the physical quantity translated? | `s05` |
| 6 | System Dynamics & Inertia | Why do physical systems lag and attenuate? | `s06` |
| 7 | Feature extraction | How to find "blink" and "focus"? | `s07`, `s07b`, `s07c` |
| 8 | Parameter measurement | What does a robot arm measure? | `s08` |
| 9 | Closed loop | Putting it all together | `s09`, `s09b`, `s10` |

Full outline (Chinese): see [`outline.md`](./outline.md).


## Repository structure

```text
SignalLab/
├── README.md              
├── LICENSE                
├── .gitignore
├── outline.md             
└── stages/              
    ├── 00-map/
    │   └── notes.md
    ├── 01-time-domain/
    │   ├── notes.md       
    │   └── s01_waveform.py 
    ├── 02-frequency/
    │   ├── notes.md
    │   ├── s02_fft.py
    │   └── s02b_pulse.py
    └── ...
```

## License

[MIT](./LICENSE)
