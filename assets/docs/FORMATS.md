# FORMATS: index

*Set `FORM`/`MC2` asset format how-it-really-works. Ground truth: the set's
original game `SET.BAS` files and the decompiled engine source under
`src/` — chunk loaders in `sklt.cpp`, `area.cpp`, `ade.cpp`, `base.cpp`,
`amesh.cpp`, `ilbm.cpp`, `bmpAnm.cpp`, `embed.cpp`. The engine reads unknown
chunks with `skipChunk()`, so a doc's "must keep" list is about lossless
rebuild, not about spoiling the original information.*

Hex dump style: `second hexdump row   hint` shows big-endian bytes; a `.` in
the ascii column is a non-printable byte. Length prefixes are big-endian
u16 unless stated.

## Container graph

```
SET.BAS
└── FORM/MC2  [[MC2]]
    └── OBJT/CLID base.class  [[OBJT]] [[CLID]]
        └── BASE  [[BASE]]
            ├── ROOT  [[NAME]]  (optional, unnamed for the set root)
            ├── OBJT/CLID embed.class + EMBD [[EMBD]]
            │       └── (EMRS, resource) pairs: [[EMRS]] → [[SKLT]] [[VBMP]] [[VANM]]
            ├── STRC (STRC_BASE flavor)  [[STRC]]
            └── KIDS  [[KIDS]]
                ├── slot 0 = vehicles   [[BASE]] trees (per visproto.lst)
                ├── slot 1 = buildings  [[BASE]] trees (per set.sdf)
                └── slot 2 = ground     [[BASE]] trees (per slurps.lst)

BASE tree unit:
└── OBJT/CLID base.class
    └── BASE
        ├── ROOT/NAME
        ├── STRC (STRC_BASE)
        └── KIDS / OBJT... sub-object recursion:
            ├── EMBD resource blobs [[EMBD]]
            ├── ADES active-detail list       [[ADES]] → [[ADE]] [[AREA]]
            ├── AMSH animated mesh            [[AMSH]] → [[ATTS]] [[OLPL]]
            ├── BANI bitmap animation link    [[BANI]] → rsrcpool/<name>.ANM [[VANM]]
            └── SKLC skeleton link            [[SKLC]]

ADE tree:
└── ADE  [[ADE]]
    ├── ROOT/NAME
    └── STRC (STRC_ADE)  class = ade.class / area.class

AREA texture plane:
└── AREA  [[AREA]]
    ├── ADE  skeleton-linked vertices
    ├── STRC (STRC_AREA flavor)
    └── OBJT (bitmap ref: [[CIBO]]/[[SKLC]] inline bitmaps)
```

## Document index

| Doc | chunk/form | role |
| --- | --- | --- |
| `FORM.md` | `FORM` | container framing, big-endian, pad rules |
| `MC2.md`  | `MC2 ` | set container built by `build_set()` |
| `OBJT.md` | `OBJT` | object node: CLID + payload |
| `CLID.md` | `CLID` | `*.class` identifier |
| `NAME.md`,`NAM2.md` | name strings | both node names and resource names |
| `BASE.md`,`ROOT.md`,`KIDS.md` | `BASE`,`ROOT`,`KIDS` | the object tree |
| `STRC.md` | `STRC` | shape/not-self-describing; BASE/ADE/AREA/BANI flavors |
| `EMBD.md` | `EMBD` | resources: class + name + resource form |
| `EMRS.md` | `EMRS` | the (class, name) pair and its engine reading |
| `SKLT.md`,`POO2.md`,`POL2.md`,`SEN2.md`,`SKLC.md` | skeleton | points/polys/attachment points/link |
| `VANM.md`,`BANI.md` | `VANM`,`BANI`, `.ANM` | bitmap animation, byte format and linking |
| `AMSH.md`,`ATTS.md`,`OLPL.md` | `AMSH` | animated mesh attrs and uv tables |
| `CIBO.md`,`OTL2.md`,`NAM2.md` | `CIBO` | outline bitmap reference |
| `ADE.md`,`AREA.md`,`ADES.md` | | detail node hierarchy incl. texture plane |
| `HEAD.md`,`BODY.md`,`BMHD.md`,`CMAP.md`,`ILBM.md`,`VBMP.md` | bitmaps | indexed pixels; set-palette coupling |

## Conventions used across these docs

- "engine" quote refers to the decompiled `src/` reader/writer pair for that
  format, cited by `file.cpp:line`.
- `[[NAME]]` style double-bracket links between docs.
- "lossless" paths are `compile.build_set(...)`/`save_to_file`-parity ones;
  see `test/test_compile.py` for the golden byte-exact set builds
  (including the plane "shell" set 46).
