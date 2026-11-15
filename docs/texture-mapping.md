# Texture mapping per set (SET.BAS -> OBJ conversion)

Computed from the engine export sidecars (``<name>.obj.mat.json`` and ``<name>.uattach``) in `/Users/af/Downloads/UA_source/export`.

Per-model png naming: `<MODEL>_<ORIG>.png`, where ORIG is the original texture resource name including its extension (e.g. `BAGGER.ILBM` -> `VP_PANZ1_BAGGER.ILBM.png`). Materials whose texture has no per-model png (animated ANM atlas names and a few pool textures) keep the `<ORIG>.png` name in the .mtl and resolve via the `<ORIG>.png` copies placed in each set's `RSRCPOOL/`.

## set1 (DATA/SET1)

### set1: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 157 | 144 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 97 | 0 | 85 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 38 | 38 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| faerrobo.ilbm | 24 | 21 | 3 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 260; models with meshes: 614; empty models: 43.

### set1: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set2 (DATA/SET2)

### set2: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 157 | 144 | 13 | 0 | 0 |
| boden2.ilbm | 111 | 0 | 103 | 8 | 0 |
| boden3.ilbm | 105 | 0 | 73 | 32 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| boden1.ilbm | 75 | 0 | 63 | 12 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| fhubi.ilbm | 55 | 41 | 14 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 39 | 38 | 1 | 0 | 0 |
| boden4.ilbm | 38 | 0 | 38 | 0 | 0 |
| taerrobo.ilbm | 33 | 7 | 26 | 0 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| faerrobo.ilbm | 31 | 21 | 10 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| fberud.ilbm | 25 | 3 | 22 | 0 | 0 |
| hype.ilbm | 25 | 0 | 23 | 2 | 0 |
| fhype.ilbm | 21 | 2 | 19 | 0 | 0 |
| fmacht.ilbm | 19 | 10 | 9 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| fcity1.ilbm | 13 | 0 | 13 | 0 | 0 |
| berud.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |
| hotshot2.anm | 9 | 9 | 0 | 0 | 9 |
| macht.ilbm | 9 | 0 | 9 | 0 | 0 |
| shrttwnd.ilbm | 8 | 4 | 4 | 0 | 0 |
| city1.ilbm | 7 | 2 | 5 | 0 | 0 |
| brgbltz.anm | 6 | 5 | 1 | 0 | 6 |

Distinct textures referenced: 252; models with meshes: 626; empty models: 43.

### set2: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| HI_CITY2 | building | HI_CITY2_BERUD.ILBM.png, HI_CITY2_BODEN2.ILBM.png, HI_CITY2_CITY1.ILBM.png | - |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| HI_HO | building | HI_HO_BERUD.ILBM.png, HI_HO_BODEN2.ILBM.png, HI_HO_CITY1.ILBM.png | - |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| HI_GS2NS | building | HI_GS2NS_HYPE.ILBM.png | - |
| HIxGS_NS | building | HIxGS_NS_HYPE.ILBM.png | - |
| HI_GS_NS | building | HI_GS_NS_HYPE.ILBM.png, HI_GS_NS_TAERROBO.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| HI_GS2_1 | building | HI_GS2_1_BODEN3.ILBM.png | - |
| HI_GS2_2 | building | HI_GS2_2_BODEN3.ILBM.png | - |
| HI_FELD2 | building | HI_FELD2_AIR1TXT.ILBM.png, HI_FELD2_BODEN3.ILBM.png, HI_FELD2_FCITY1.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| HI_GS1_1 | building | HI_GS1_1_BODEN3.ILBM.png | - |
| HI_GS1_2 | building | HI_GS1_2_BODEN3.ILBM.png | - |
| HIYFELD2 | building | HIYFELD2_BODEN3.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| HI_HUKL1 | building | HI_HUKL1_BODEN3.ILBM.png | - |
| HI_HUKL2 | building | HI_HUKL2_BODEN3.ILBM.png | - |
| HI_HUKL3 | building | HI_HUKL3_BODEN1.ILBM.png, HI_HUKL3_BODEN3.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| GS_MONT1 | building | GS_MONT1_BODEN1.ILBM.png, GS_MONT1_BODEN3.ILBM.png | - |
| GS_MONT3 | building | GS_MONT3_BODEN3.ILBM.png | - |
| GS_MONT2 | building | GS_MONT2_BODEN3.ILBM.png | - |
| GS_MONT4 | building | GS_MONT4_BODEN3.ILBM.png | - |
| GS_MONT5 | building | GS_MONT5_BODEN1.ILBM.png, GS_MONT5_BODEN3.ILBM.png | - |
| GS_HUkl1 | building | GS_HUkl1_BODEN3.ILBM.png | - |
| GS_LOCH1 | building | GS_LOCH1_BODEN3.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| HI_BIG | building | HI_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| HI_GS_X | building | HI_GS_X_BODEN3.ILBM.png, HI_GS_X_BODEN4.ILBM.png | - |
| HI_GS_X2 | building | HI_GS_X2_BODEN3.ILBM.png, HI_GS_X2_BODEN4.ILBM.png | - |
| HI_GS_OW | building | HI_GS_OW_HYPE.ILBM.png, HI_GS_OW_TAERROBO.ILBM.png | - |
| HIxGS_OW | building | HIxGS_OW_HYPE.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| HI_GS_A | building | HI_GS_A_BODEN3.ILBM.png, HI_GS_A_BODEN4.ILBM.png | - |
| HI_GS_A1 | building | HI_GS_A1_BODEN3.ILBM.png, HI_GS_A1_BODEN4.ILBM.png, HI_GS_A1_TAERROBO.ILBM.png | - |
| HIxGS_A1 | building | HIxGS_A1_BODEN3.ILBM.png, HIxGS_A1_BODEN4.ILBM.png | - |
| HI_GS2OW | building | HI_GS2OW_HYPE.ILBM.png, HI_GS2OW_TAERROBO.ILBM.png | - |
| HIxGS2OW | building | HIxGS2OW_HYPE.ILBM.png | - |
| HI_FELD1 | building | HI_FELD1_BODEN3.ILBM.png, HI_FELD1_FCITY1.ILBM.png, HI_FELD1_FHUBI.ILBM.png | - |
| HIyFELD1 | building | HIyFELD1_BODEN3.ILBM.png, HIyFELD1_FHUBI.ILBM.png | - |
| HI_SCHL4 | building | HI_SCHL4_BODEN1.ILBM.png, HI_SCHL4_BODEN3.ILBM.png | - |
| HI_SCHL5 | building | HI_SCHL5_BODEN1.ILBM.png, HI_SCHL5_BODEN3.ILBM.png | - |
| HI_SCHL6 | building | HI_SCHL6_BODEN1.ILBM.png, HI_SCHL6_BODEN3.ILBM.png | - |
| HI_HUKL4 | building | HI_HUKL4_BODEN1.ILBM.png, HI_HUKL4_BODEN3.ILBM.png | - |
| HI_KMPKT | building | HI_KMPKT_BODEN2.ILBM.png | - |
| HI_RIES1 | building | HI_RIES1_BODEN3.ILBM.png, HI_RIES1_TAERROBO.ILBM.png | - |
| HIxRIES1 | building | HIxRIES1_BODEN3.ILBM.png, HIxRIES1_TAERROBO.ILBM.png | - |
| HI_RIES2 | building | HI_RIES2_BODEN3.ILBM.png, HI_RIES2_TAERROBO.ILBM.png | - |
| HIxRIES2 | building | HIxRIES2_BODEN3.ILBM.png, HIxRIES2_TAERROBO.ILBM.png | - |
| HI_RIES3 | building | HI_RIES3_BODEN3.ILBM.png, HI_RIES3_TAERROBO.ILBM.png | - |
| HIxRIES3 | building | HIxRIES3_BODEN3.ILBM.png, HIxRIES3_TAERROBO.ILBM.png | - |
| HI_RIES0 | building | HI_RIES0_BODEN3.ILBM.png, HI_RIES0_TAERROBO.ILBM.png | - |
| HIxRIES0 | building | HIxRIES0_BODEN3.ILBM.png, HIxRIES0_TAERROBO.ILBM.png | - |
| HIyRIES0 | building | HIyRIES0_BODEN3.ILBM.png, HIyRIES0_TAERROBO.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| HI_GR_1 | building | HI_GR_1_BODEN2.ILBM.png, HI_GR_1_TAERROBO.ILBM.png | - |
| HI_GR_2 | building | HI_GR_2_BODEN2.ILBM.png | - |
| HIxGR_1 | building | HIxGR_1_BODEN2.ILBM.png | - |
| HIzGR_1 | building | HIzGR_1_BODEN4.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| HI_TAERK | building | HI_TAERK_BODEN3.ILBM.png, HI_TAERK_TAERROBO.ILBM.png | - |
| HIXTAERK | building | HIXTAERK_BODEN3.ILBM.png, HIXTAERK_FAERROBO.ILBM.png, HIXTAERK_TAERROBO.ILBM.png | - |
| GS_NSTR0 | building | GS_NSTR0_BODEN3.ILBM.png, GS_NSTR0_HYPE.ILBM.png | - |
| GS_NSTR1 | building | GS_NSTR1_BODEN3.ILBM.png, GS_NSTR1_HYPE.ILBM.png | - |
| GS_NSTR2 | building | GS_NSTR2_BODEN3.ILBM.png, GS_NSTR2_HYPE.ILBM.png | - |
| GS_NSTR3 | building | GS_NSTR3_BODEN3.ILBM.png, GS_NSTR3_HYPE.ILBM.png | - |
| GS_BAUR2 | building | GS_BAUR2_BODEN3.ILBM.png, GS_BAUR2_TAERROBO.ILBM.png | - |
| GSxBAUR2 | building | GSxBAUR2_BODEN3.ILBM.png, GSxBAUR2_FAERROBO.ILBM.png | - |
| GSyBAUR2 | building | GSyBAUR2_BODEN3.ILBM.png, GSyBAUR2_FAERROBO.ILBM.png | - |
| GSzBAUR2 | building | GSzBAUR2_BODEN3.ILBM.png | - |
| GS_BAUR3 | building | GS_BAUR3_BODEN3.ILBM.png, GS_BAUR3_TAERROBO.ILBM.png | - |
| GSxBAUR3 | building | GSxBAUR3_BODEN3.ILBM.png, GSxBAUR3_FAERROBO.ILBM.png | - |
| GSyBAUR3 | building | GSyBAUR3_BODEN3.ILBM.png, GSyBAUR3_FAERROBO.ILBM.png | - |
| GSzBAUR3 | building | GSzBAUR3_BODEN3.ILBM.png | - |
| GS_NSTR4 | building | GS_NSTR4_BODEN4.ILBM.png, GS_NSTR4_HYPE.ILBM.png | - |
| GS_NSTR5 | building | GS_NSTR5_BODEN4.ILBM.png, GS_NSTR5_HYPE.ILBM.png | - |
| GS_NSTR6 | building | GS_NSTR6_BODEN4.ILBM.png, GS_NSTR6_HYPE.ILBM.png | - |
| GS_NSTR7 | building | GS_NSTR7_BODEN3.ILBM.png, GS_NSTR7_BODEN4.ILBM.png, GS_NSTR7_HYPE.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| GS_DHNEU | building | GS_DHNEU_BERUD.ILBM.png, GS_DHNEU_BODEN3.ILBM.png, GS_DHNEU_CITY1.ILBM.png | - |
| GSxDHNEU | building | GSxDHNEU_BODEN3.ILBM.png, GSxDHNEU_FBERUD.ILBM.png, GSxDHNEU_FCITY1.ILBM.png | - |
| GSyDHNEU | building | GSyDHNEU_BODEN3.ILBM.png, GSyDHNEU_FBERUD.ILBM.png, GSyDHNEU_FCITY1.ILBM.png | - |
| GSzDHNEU | building | GSzDHNEU_BODEN4.ILBM.png | - |
| HI_BERGA | building | HI_BERGA_BODEN3.ILBM.png | - |
| HI_BERGB | building | HI_BERGB_BODEN3.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| HI_MACHT | building | HI_MACHT_BERUD.ILBM.png, HI_MACHT_BODEN2.ILBM.png, HI_MACHT_MACHT.ILBM.png | - |
| HIxMACHT | building | HIxMACHT_BODEN2.ILBM.png, HIxMACHT_FBERUD.ILBM.png, HIxMACHT_FMACHT.ILBM.png | - |
| HIyMACHT | building | HIyMACHT_BODEN2.ILBM.png, HIyMACHT_FBERUD.ILBM.png, HIyMACHT_FMACHT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| GS_TOR | building | GS_TOR_BODEN3.ILBM.png, GS_TOR_TAERROBO.ILBM.png | - |
| GSxTOR | building | GSxTOR_BODEN3.ILBM.png, GSxTOR_FAERROBO.ILBM.png | - |
| GSyTOR | building | GSyTOR_BODEN3.ILBM.png, GSyTOR_FAERROBO.ILBM.png | - |
| GSzTOR | building | GSzTOR_BODEN3.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| HIzHUKL1 | building | HIzHUKL1_BODEN3.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| GS_LUUCH | building | GS_LUUCH_BODEN4.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| GS_SCHL3 | building | GS_SCHL3_BODEN1.ILBM.png, GS_SCHL3_BODEN3.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| GS_BERG1 | building | GS_BERG1_BODEN3.ILBM.png, GS_BERG1_BODEN4.ILBM.png | - |
| GS_BERG2 | building | GS_BERG2_BODEN3.ILBM.png, GS_BERG2_BODEN4.ILBM.png | - |
| GS_STRE | building | GS_STRE_HYPE.ILBM.png | - |
| GS_STREA | building | GS_STREA_BODEN3.ILBM.png, GS_STREA_BODEN4.ILBM.png | - |
| GS_STREB | building | GS_STREB_BODEN3.ILBM.png, GS_STREB_BODEN4.ILBM.png | - |
| GS_STREC | building | GS_STREC_BODEN3.ILBM.png, GS_STREC_BODEN4.ILBM.png | - |
| GS_STRED | building | GS_STRED_HYPE.ILBM.png | - |
| GS_STREE | building | GS_STREE_BODEN4.ILBM.png, GS_STREE_HYPE.ILBM.png | - |
| GS_STREF | building | GS_STREF_BODEN4.ILBM.png, GS_STREF_HYPE.ILBM.png | - |
| GS_STREz | building | GS_STREz_BODEN4.ILBM.png, GS_STREz_FHUBI.ILBM.png, GS_STREz_HYPE.ILBM.png | - |
| GSxSTREz | building | GSxSTREz_BODEN4.ILBM.png, GSxSTREz_FHUBI.ILBM.png, GSxSTREz_HYPE.ILBM.png | - |
| GSzSTREz | building | GSzSTREz_BODEN4.ILBM.png, GSzSTREz_HYPE.ILBM.png | - |
| GS_SCHL1 | building | GS_SCHL1_BODEN1.ILBM.png, GS_SCHL1_BODEN3.ILBM.png | - |
| GS_SCHL2 | building | GS_SCHL2_BODEN1.ILBM.png, GS_SCHL2_BODEN3.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set3 (DATA/SET3)

### set3: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 157 | 144 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 97 | 0 | 85 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 38 | 38 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| faerrobo.ilbm | 24 | 21 | 3 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 260; models with meshes: 614; empty models: 43.

### set3: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set4 (DATA/SET4)

### set4: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 157 | 144 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 98 | 0 | 86 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 38 | 38 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 35 | 0 | 3 | 32 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| faerrobo.ilbm | 24 | 21 | 3 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| taerrobo.ilbm | 15 | 7 | 8 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 257; models with meshes: 616; empty models: 43.

### set4: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ET_EMPTY | building | ET_EMPTY_BODEN2.ILBM.png | - |
| ER_EMTPY | building | ER_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ET_CITY1 | building | ET_CITY1_BERUD.ILBM.png, ET_CITY1_BODEN2.ILBM.png, ET_CITY1_CITY1.ILBM.png | - |
| ETxCITY1 | building | ETxCITY1_BODEN2.ILBM.png, ETxCITY1_FBERUD.ILBM.png, ETxCITY1_FCITY1.ILBM.png | - |
| ETyCITY1 | building | ETyCITY1_BODEN2.ILBM.png, ETyCITY1_FBERUD.ILBM.png, ETyCITY1_FCITY1.ILBM.png | - |
| ETzCITYn | building | ETzCITYn_BODEN2.ILBM.png | - |
| ET_CITY2 | building | ET_CITY2_BERUD.ILBM.png, ET_CITY2_BODEN2.ILBM.png, ET_CITY2_CITY1.ILBM.png | - |
| ETxCITY2 | building | ETxCITY2_BODEN2.ILBM.png, ETxCITY2_FBERUD.ILBM.png, ETxCITY2_FCITY1.ILBM.png | - |
| ETyCITY2 | building | ETyCITY2_BODEN2.ILBM.png, ETyCITY2_FBERUD.ILBM.png, ETyCITY2_FCITY1.ILBM.png | - |
| ET_MUSE | building | ET_MUSE_BERUD.ILBM.png, ET_MUSE_BODEN2.ILBM.png, ET_MUSE_CITY1.ILBM.png | - |
| ETxMUSE | building | ETxMUSE_BODEN2.ILBM.png, ETxMUSE_FBERUD.ILBM.png, ETxMUSE_FCITY1.ILBM.png | - |
| ETyMUSE | building | ETyMUSE_BODEN2.ILBM.png, ETyMUSE_FBERUD.ILBM.png, ETyMUSE_FCITY1.ILBM.png | - |
| ETzMUSE | building | ETzMUSE_BODEN2.ILBM.png | - |
| ET_HO | building | ET_HO_BERUD.ILBM.png, ET_HO_BODEN2.ILBM.png, ET_HO_CITY1.ILBM.png | - |
| ETxHO | building | ETxHO_BODEN2.ILBM.png, ETxHO_FBERUD.ILBM.png, ETxHO_FCITY1.ILBM.png | - |
| ETyHO | building | ETyHO_BODEN2.ILBM.png, ETyHO_FBERUD.ILBM.png, ETyHO_FCITY1.ILBM.png | - |
| ETzHO | building | ETzHO_BODEN2.ILBM.png, ETzHO_FBERUD.ILBM.png, ETzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ET_KRATR | building | ET_KRATR_BODEN2.ILBM.png | - |
| ET_KRAT2 | building | ET_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| ER_FLECK | building | ER_FLECK_BODEN2.ILBM.png | - |
| ER_KRAT1 | building | ER_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| ET_SLUM1 | building | ET_SLUM1_BERUD.ILBM.png, ET_SLUM1_BODEN2.ILBM.png | - |
| ETxSLUM1 | building | ETxSLUM1_BODEN2.ILBM.png, ETxSLUM1_FBERUD.ILBM.png | - |
| EtySLUM1 | building | EtySLUM1_BODEN2.ILBM.png, EtySLUM1_FBERUD.ILBM.png | - |
| ER_SLUM1 | building | ER_SLUM1_BERUD.ILBM.png, ER_SLUM1_BODEN1.ILBM.png | - |
| ERxSLUM1 | building | ERxSLUM1_BODEN1.ILBM.png, ERxSLUM1_FBERUD.ILBM.png | - |
| ERySLUM1 | building | ERySLUM1_BODEN1.ILBM.png, ERySLUM1_FBERUD.ILBM.png | - |
| ER_SLUM3 | building | ER_SLUM3_BODEN1.ILBM.png, ER_SLUM3_SHRTTWND.ILBM.png | - |
| ERxSLUM3 | building | ERxSLUM3_BODEN1.ILBM.png, ERxSLUM3_FHRTTWND.ILBM.png | - |
| ERySLUM3 | building | ERySLUM3_BODEN1.ILBM.png, ERySLUM3_FHRTTWND.ILBM.png | - |
| ERzSLUM3 | building | ERzSLUM3_BODEN2.ILBM.png | - |
| ER_SLUM2 | building | ER_SLUM2_BERUD.ILBM.png, ER_SLUM2_BODEN1.ILBM.png | - |
| ERxSLUM2 | building | ERxSLUM2_BODEN1.ILBM.png, ERxSLUM2_FBERUD.ILBM.png | - |
| ERySLUM2 | building | ERySLUM2_BODEN1.ILBM.png, ERySLUM2_BODEN2.ILBM.png, ERySLUM2_FBERUD.ILBM.png | - |
| ERzSLUM2 | building | ERzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| ER_HUKKL | building | ER_HUKKL_BODEN1.ILBM.png | - |
| ER_SANFT | building | ER_SANFT_BODEN1.ILBM.png | - |
| ET_KMPKT | building | ET_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set5 (DATA/SET5)

### set5: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 157 | 144 | 13 | 0 | 0 |
| boden2.ilbm | 109 | 0 | 101 | 8 | 0 |
| boden3.ilbm | 96 | 0 | 64 | 32 | 0 |
| boden1.ilbm | 86 | 0 | 74 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 59 | 33 | 26 | 0 | 0 |
| fhubi.ilbm | 55 | 41 | 14 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 39 | 38 | 1 | 0 | 0 |
| boden4.ilbm | 38 | 0 | 38 | 0 | 0 |
| hype.ilbm | 37 | 0 | 35 | 2 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| faerrobo.ilbm | 31 | 21 | 10 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| taerrobo.ilbm | 24 | 7 | 17 | 0 | 0 |
| fhype.ilbm | 24 | 2 | 22 | 0 | 0 |
| fberud.ilbm | 23 | 3 | 20 | 0 | 0 |
| fmacht.ilbm | 19 | 10 | 9 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| macht.ilbm | 12 | 0 | 12 | 0 | 0 |
| fcity1.ilbm | 11 | 0 | 11 | 0 | 0 |
| berud.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |
| hotshot2.anm | 9 | 9 | 0 | 0 | 9 |
| shrttwnd.ilbm | 8 | 4 | 4 | 0 | 0 |
| city1.ilbm | 7 | 2 | 5 | 0 | 0 |
| brgbltz.anm | 6 | 5 | 1 | 0 | 6 |

Distinct textures referenced: 252; models with meshes: 632; empty models: 43.

### set5: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | vehicle | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | vehicle | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | vehicle | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | vehicle | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | vehicle | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| WS_CITY2 | building | WS_CITY2_BERUD.ILBM.png, WS_CITY2_BODEN2.ILBM.png, WS_CITY2_CITY1.ILBM.png | - |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| WS_HO | building | WS_HO_BERUD.ILBM.png, WS_HO_BODEN2.ILBM.png, WS_HO_CITY1.ILBM.png | - |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| HI_GS2NS | building | HI_GS2NS_HYPE.ILBM.png | - |
| HIxGS_NS | building | HIxGS_NS_HYPE.ILBM.png | - |
| HI_GS_NS | building | HI_GS_NS_HYPE.ILBM.png, HI_GS_NS_TAERROBO.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| HI_GS2_1 | building | HI_GS2_1_BODEN3.ILBM.png | - |
| HI_GS2_2 | building | HI_GS2_2_BODEN3.ILBM.png | - |
| HI_FELD2 | building | HI_FELD2_AIR1TXT.ILBM.png, HI_FELD2_BODEN3.ILBM.png, HI_FELD2_FCITY1.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| HI_GS1_1 | building | HI_GS1_1_BODEN3.ILBM.png | - |
| HI_GS1_2 | building | HI_GS1_2_BODEN3.ILBM.png | - |
| HIYFELD2 | building | HIYFELD2_BODEN3.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| HI_HUKL1 | building | HI_HUKL1_BODEN3.ILBM.png | - |
| HI_HUKL2 | building | HI_HUKL2_BODEN3.ILBM.png | - |
| HI_HUKL3 | building | HI_HUKL3_BODEN1.ILBM.png, HI_HUKL3_BODEN3.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| GS_MONT1 | building | GS_MONT1_BODEN1.ILBM.png, GS_MONT1_BODEN3.ILBM.png | - |
| GS_MONT3 | building | GS_MONT3_BODEN3.ILBM.png | - |
| GS_MONT2 | building | GS_MONT2_BODEN3.ILBM.png | - |
| GS_MONT4 | building | GS_MONT4_BODEN3.ILBM.png | - |
| GS_MONT5 | building | GS_MONT5_BODEN1.ILBM.png, GS_MONT5_BODEN3.ILBM.png | - |
| GS_HUkl1 | building | GS_HUkl1_BODEN3.ILBM.png | - |
| GS_LOCH1 | building | GS_LOCH1_BODEN3.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| HI_BIG | building | HI_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| HI_GS_X | building | HI_GS_X_BODEN3.ILBM.png, HI_GS_X_BODEN4.ILBM.png | - |
| HI_GS_X2 | building | HI_GS_X2_BODEN3.ILBM.png, HI_GS_X2_BODEN4.ILBM.png | - |
| HI_GS_OW | building | HI_GS_OW_HYPE.ILBM.png, HI_GS_OW_TAERROBO.ILBM.png | - |
| HIxGS_OW | building | HIxGS_OW_HYPE.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| HI_GS_A | building | HI_GS_A_BODEN3.ILBM.png, HI_GS_A_BODEN4.ILBM.png | - |
| HI_GS_A1 | building | HI_GS_A1_BODEN3.ILBM.png, HI_GS_A1_BODEN4.ILBM.png, HI_GS_A1_TAERROBO.ILBM.png | - |
| HIxGS_A1 | building | HIxGS_A1_BODEN3.ILBM.png, HIxGS_A1_BODEN4.ILBM.png | - |
| HI_GS2OW | building | HI_GS2OW_HYPE.ILBM.png, HI_GS2OW_TAERROBO.ILBM.png | - |
| HIxGS2OW | building | HIxGS2OW_HYPE.ILBM.png | - |
| HI_FELD1 | building | HI_FELD1_BODEN3.ILBM.png, HI_FELD1_FCITY1.ILBM.png, HI_FELD1_FHUBI.ILBM.png | - |
| HIyFELD1 | building | HIyFELD1_BODEN3.ILBM.png, HIyFELD1_FHUBI.ILBM.png | - |
| HI_SCHL4 | building | HI_SCHL4_BODEN1.ILBM.png, HI_SCHL4_BODEN3.ILBM.png | - |
| HI_SCHL5 | building | HI_SCHL5_BODEN1.ILBM.png, HI_SCHL5_BODEN3.ILBM.png | - |
| HI_SCHL6 | building | HI_SCHL6_BODEN1.ILBM.png, HI_SCHL6_BODEN3.ILBM.png | - |
| HI_HUKL4 | building | HI_HUKL4_BODEN1.ILBM.png, HI_HUKL4_BODEN3.ILBM.png | - |
| HI_KMPKT | building | HI_KMPKT_BODEN2.ILBM.png | - |
| XX_OELP1 | building | XX_OELP1_BODEN1.ILBM.png, XX_OELP1_FHYPE.ILBM.png, XX_OELP1_MTL.ILBM.png | - |
| XXxOELP1 | building | XXxOELP1_BODEN1.ILBM.png, XXxOELP1_FHYPE.ILBM.png | - |
| WG_pyram | building | WG_pyram_HYPE.ILBM.png | - |
| WGxpyram | building | WGxpyram_HYPE.ILBM.png | - |
| WGypyram | building | WGypyram_HYPE.ILBM.png | - |
| WG_STELE | building | WG_STELE_BODEN1.ILBM.png, WG_STELE_MACHT.ILBM.png | - |
| WGxSTELE | building | WGxSTELE_BODEN1.ILBM.png, WGxSTELE_MACHT.ILBM.png | - |
| WGySTELE | building | WGySTELE_BODEN1.ILBM.png, WGySTELE_MACHT.ILBM.png | - |
| WG_SPHNX | building | WG_SPHNX_BODEN1.ILBM.png, WG_SPHNX_FHYPE.ILBM.png, WG_SPHNX_HYPE.ILBM.png | - |
| WGxSPHNX | building | WGxSPHNX_BODEN1.ILBM.png, WGxSPHNX_HYPE.ILBM.png | - |
| WGySPHNX | building | WGySPHNX_BODEN1.ILBM.png, WGySPHNX_HYPE.ILBM.png | - |
| WG_SMALL | building | WG_SMALL_HYPE.ILBM.png | - |
| WGxSMALL | building | WGxSMALL_HYPE.ILBM.png | - |
| WGySMALL | building | WGySMALL_HYPE.ILBM.png | - |
| HI_GR_1 | building | HI_GR_1_BODEN2.ILBM.png, HI_GR_1_TAERROBO.ILBM.png | - |
| HI_GR_2 | building | HI_GR_2_BODEN2.ILBM.png | - |
| HIxGR_1 | building | HIxGR_1_BODEN2.ILBM.png | - |
| HIzGR_1 | building | HIzGR_1_BODEN4.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| wg_tor | building | wg_tor_BODEN1.ILBM.png, wg_tor_HYPE.ILBM.png | - |
| wgxtor | building | wgxtor_BODEN1.ILBM.png, wgxtor_HYPE.ILBM.png | - |
| wgytor | building | wgytor_BODEN1.ILBM.png, wgytor_HYPE.ILBM.png | - |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| GS_BAUR2 | building | GS_BAUR2_BODEN3.ILBM.png, GS_BAUR2_TAERROBO.ILBM.png | - |
| GSxBAUR2 | building | GSxBAUR2_BODEN3.ILBM.png, GSxBAUR2_FAERROBO.ILBM.png | - |
| GSyBAUR2 | building | GSyBAUR2_BODEN3.ILBM.png, GSyBAUR2_FAERROBO.ILBM.png | - |
| GSzBAUR2 | building | GSzBAUR2_BODEN3.ILBM.png | - |
| GS_BAUR3 | building | GS_BAUR3_BODEN3.ILBM.png, GS_BAUR3_TAERROBO.ILBM.png | - |
| GSxBAUR3 | building | GSxBAUR3_BODEN3.ILBM.png, GSxBAUR3_FAERROBO.ILBM.png | - |
| GSyBAUR3 | building | GSyBAUR3_BODEN3.ILBM.png, GSyBAUR3_FAERROBO.ILBM.png | - |
| GSzBAUR3 | building | GSzBAUR3_BODEN3.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| HI_TAERK | building | HI_TAERK_BODEN3.ILBM.png, HI_TAERK_TAERROBO.ILBM.png | - |
| HIXTAERK | building | HIXTAERK_BODEN3.ILBM.png, HIXTAERK_FAERROBO.ILBM.png, HIXTAERK_TAERROBO.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| GS_DHNEU | building | GS_DHNEU_BERUD.ILBM.png, GS_DHNEU_BODEN3.ILBM.png, GS_DHNEU_CITY1.ILBM.png | - |
| GSxDHNEU | building | GSxDHNEU_BODEN3.ILBM.png, GSxDHNEU_FBERUD.ILBM.png, GSxDHNEU_FCITY1.ILBM.png | - |
| GSyDHNEU | building | GSyDHNEU_BODEN3.ILBM.png, GSyDHNEU_FBERUD.ILBM.png, GSyDHNEU_FCITY1.ILBM.png | - |
| GSzDHNEU | building | GSzDHNEU_BODEN4.ILBM.png | - |
| HIzHUKL1 | building | HIzHUKL1_BODEN3.ILBM.png | - |
| HI_BERGA | building | HI_BERGA_BODEN3.ILBM.png | - |
| HI_BERGB | building | HI_BERGB_BODEN3.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| HI_MACHT | building | HI_MACHT_BERUD.ILBM.png, HI_MACHT_BODEN2.ILBM.png, HI_MACHT_MACHT.ILBM.png | - |
| HIxMACHT | building | HIxMACHT_BODEN2.ILBM.png, HIxMACHT_FBERUD.ILBM.png, HIxMACHT_FMACHT.ILBM.png | - |
| HIyMACHT | building | HIyMACHT_BODEN2.ILBM.png, HIyMACHT_FBERUD.ILBM.png, HIyMACHT_FMACHT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| GS_TOR | building | GS_TOR_BODEN3.ILBM.png, GS_TOR_TAERROBO.ILBM.png | - |
| GSxTOR | building | GSxTOR_BODEN3.ILBM.png, GSxTOR_FAERROBO.ILBM.png | - |
| GSyTOR | building | GSyTOR_BODEN3.ILBM.png, GSyTOR_FAERROBO.ILBM.png | - |
| GSzTOR | building | GSzTOR_BODEN3.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| GS_NSTR0 | building | GS_NSTR0_BODEN3.ILBM.png, GS_NSTR0_HYPE.ILBM.png | - |
| GS_NSTR1 | building | GS_NSTR1_BODEN3.ILBM.png, GS_NSTR1_HYPE.ILBM.png | - |
| GS_NSTR2 | building | GS_NSTR2_BODEN3.ILBM.png, GS_NSTR2_HYPE.ILBM.png | - |
| GS_NSTR3 | building | GS_NSTR3_BODEN3.ILBM.png, GS_NSTR3_HYPE.ILBM.png | - |
| GS_NSTR4 | building | GS_NSTR4_BODEN4.ILBM.png, GS_NSTR4_HYPE.ILBM.png | - |
| GS_NSTR5 | building | GS_NSTR5_BODEN4.ILBM.png, GS_NSTR5_HYPE.ILBM.png | - |
| GS_NSTR6 | building | GS_NSTR6_BODEN4.ILBM.png, GS_NSTR6_HYPE.ILBM.png | - |
| GS_NSTR7 | building | GS_NSTR7_BODEN3.ILBM.png, GS_NSTR7_BODEN4.ILBM.png, GS_NSTR7_HYPE.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| GS_LUUCH | building | GS_LUUCH_BODEN4.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| GS_SCHL3 | building | GS_SCHL3_BODEN1.ILBM.png, GS_SCHL3_BODEN3.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| GS_BERG1 | building | GS_BERG1_BODEN3.ILBM.png, GS_BERG1_BODEN4.ILBM.png | - |
| GS_BERG2 | building | GS_BERG2_BODEN3.ILBM.png, GS_BERG2_BODEN4.ILBM.png | - |
| GS_STRE | building | GS_STRE_HYPE.ILBM.png | - |
| GS_STREA | building | GS_STREA_BODEN3.ILBM.png, GS_STREA_BODEN4.ILBM.png | - |
| GS_STREB | building | GS_STREB_BODEN3.ILBM.png, GS_STREB_BODEN4.ILBM.png | - |
| GS_STREC | building | GS_STREC_BODEN3.ILBM.png, GS_STREC_BODEN4.ILBM.png | - |
| GS_STRED | building | GS_STRED_HYPE.ILBM.png | - |
| GS_STREE | building | GS_STREE_BODEN4.ILBM.png, GS_STREE_HYPE.ILBM.png | - |
| GS_STREF | building | GS_STREF_BODEN4.ILBM.png, GS_STREF_HYPE.ILBM.png | - |
| GS_STREz | building | GS_STREz_BODEN4.ILBM.png, GS_STREz_FHUBI.ILBM.png, GS_STREz_HYPE.ILBM.png | - |
| GSxSTREz | building | GSxSTREz_BODEN4.ILBM.png, GSxSTREz_FHUBI.ILBM.png, GSxSTREz_HYPE.ILBM.png | - |
| GSzSTREz | building | GSzSTREz_BODEN4.ILBM.png, GSzSTREz_HYPE.ILBM.png | - |
| GS_SCHL1 | building | GS_SCHL1_BODEN1.ILBM.png, GS_SCHL1_BODEN3.ILBM.png | - |
| GS_SCHL2 | building | GS_SCHL2_BODEN1.ILBM.png, GS_SCHL2_BODEN3.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set6 (DATA/SET6)

### set6: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 162 | 144 | 18 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 93 | 0 | 81 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 66 | 66 | 0 | 0 | 0 |
| mtl.ilbm | 60 | 33 | 27 | 0 | 0 |
| genes4-1.anm | 51 | 51 | 0 | 0 | 51 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| boden5.ilbm | 44 | 2 | 20 | 22 | 0 |
| air1txt.ilbm | 38 | 38 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| genes3-1.anm | 30 | 30 | 0 | 0 | 30 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| faerrobo.ilbm | 24 | 21 | 3 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 18 | 18 | 0 | 0 | 18 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 275; models with meshes: 625; empty models: 43.

### set6: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_ENDL1 | building | ST_ENDL1_BODEN5.ILBM.png, ST_ENDL1_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL2 | building | ST_ENDL2_BODEN5.ILBM.png, ST_ENDL2_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL3 | building | ST_ENDL3_BODEN5.ILBM.png, ST_ENDL3_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL4 | building | ST_ENDL4_BODEN5.ILBM.png, ST_ENDL4_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL5 | building | ST_ENDL5_BODEN5.ILBM.png, ST_ENDL5_FX2.ILBM.png, ST_ENDL5_MTL.ILBM.png | 0312970A.ANM.png, 0312970B.ANM.png, 0312970C.ANM.png, 0312970D.ANM.png, 0312970E.ANM.png, 0312970F.ANM.png, 0312970G.ANM.png, 14099701.ANM.png, 14099702.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| STxENDL1 | building | STxENDL1_BODEN5.ILBM.png | - |
| STxENDL2 | building | STxENDL2_BODEN5.ILBM.png | - |
| STxENDL3 | building | STxENDL3_BODEN5.ILBM.png | - |
| STxENDL4 | building | STxENDL4_BODEN5.ILBM.png | - |
| STxENDL5 | building | STxENDL5_BODEN5.ILBM.png, STxENDL5_MTL.ILBM.png | 14099701.ANM.png |
| ST_MLEER | building | ST_MLEER_BODEN5.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set1_xp (dataxp/Set1)

### set1_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 163 | 150 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 97 | 0 | 85 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 40 | 40 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| faerrobo.ilbm | 30 | 27 | 3 | 0 | 0 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 270; models with meshes: 625; empty models: 43.

### set1_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set2_xp (dataxp/Set2)

### set2_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 163 | 150 | 13 | 0 | 0 |
| boden2.ilbm | 111 | 0 | 103 | 8 | 0 |
| boden3.ilbm | 105 | 0 | 73 | 32 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| boden1.ilbm | 75 | 0 | 63 | 12 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| fhubi.ilbm | 55 | 41 | 14 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 41 | 40 | 1 | 0 | 0 |
| boden4.ilbm | 38 | 0 | 38 | 0 | 0 |
| faerrobo.ilbm | 37 | 27 | 10 | 0 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| taerrobo.ilbm | 33 | 7 | 26 | 0 | 0 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fberud.ilbm | 25 | 3 | 22 | 0 | 0 |
| hype.ilbm | 25 | 0 | 23 | 2 | 0 |
| fhype.ilbm | 21 | 2 | 19 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| fmacht.ilbm | 19 | 10 | 9 | 0 | 0 |
| fcity1.ilbm | 13 | 0 | 13 | 0 | 0 |
| berud.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |
| hotshot2.anm | 9 | 9 | 0 | 0 | 9 |
| macht.ilbm | 9 | 0 | 9 | 0 | 0 |
| shrttwnd.ilbm | 8 | 4 | 4 | 0 | 0 |
| city1.ilbm | 7 | 2 | 5 | 0 | 0 |
| brgbltz.anm | 6 | 5 | 1 | 0 | 6 |

Distinct textures referenced: 262; models with meshes: 637; empty models: 43.

### set2_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| HI_CITY2 | building | HI_CITY2_BERUD.ILBM.png, HI_CITY2_BODEN2.ILBM.png, HI_CITY2_CITY1.ILBM.png | - |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| HI_HO | building | HI_HO_BERUD.ILBM.png, HI_HO_BODEN2.ILBM.png, HI_HO_CITY1.ILBM.png | - |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| HI_GS2NS | building | HI_GS2NS_HYPE.ILBM.png | - |
| HIxGS_NS | building | HIxGS_NS_HYPE.ILBM.png | - |
| HI_GS_NS | building | HI_GS_NS_HYPE.ILBM.png, HI_GS_NS_TAERROBO.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| HI_GS2_1 | building | HI_GS2_1_BODEN3.ILBM.png | - |
| HI_GS2_2 | building | HI_GS2_2_BODEN3.ILBM.png | - |
| HI_FELD2 | building | HI_FELD2_AIR1TXT.ILBM.png, HI_FELD2_BODEN3.ILBM.png, HI_FELD2_FCITY1.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| HI_GS1_1 | building | HI_GS1_1_BODEN3.ILBM.png | - |
| HI_GS1_2 | building | HI_GS1_2_BODEN3.ILBM.png | - |
| HIYFELD2 | building | HIYFELD2_BODEN3.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| HI_HUKL1 | building | HI_HUKL1_BODEN3.ILBM.png | - |
| HI_HUKL2 | building | HI_HUKL2_BODEN3.ILBM.png | - |
| HI_HUKL3 | building | HI_HUKL3_BODEN1.ILBM.png, HI_HUKL3_BODEN3.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| GS_MONT1 | building | GS_MONT1_BODEN1.ILBM.png, GS_MONT1_BODEN3.ILBM.png | - |
| GS_MONT3 | building | GS_MONT3_BODEN3.ILBM.png | - |
| GS_MONT2 | building | GS_MONT2_BODEN3.ILBM.png | - |
| GS_MONT4 | building | GS_MONT4_BODEN3.ILBM.png | - |
| GS_MONT5 | building | GS_MONT5_BODEN1.ILBM.png, GS_MONT5_BODEN3.ILBM.png | - |
| GS_HUkl1 | building | GS_HUkl1_BODEN3.ILBM.png | - |
| GS_LOCH1 | building | GS_LOCH1_BODEN3.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| HI_BIG | building | HI_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| HI_GS_X | building | HI_GS_X_BODEN3.ILBM.png, HI_GS_X_BODEN4.ILBM.png | - |
| HI_GS_X2 | building | HI_GS_X2_BODEN3.ILBM.png, HI_GS_X2_BODEN4.ILBM.png | - |
| HI_GS_OW | building | HI_GS_OW_HYPE.ILBM.png, HI_GS_OW_TAERROBO.ILBM.png | - |
| HIxGS_OW | building | HIxGS_OW_HYPE.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| HI_GS_A | building | HI_GS_A_BODEN3.ILBM.png, HI_GS_A_BODEN4.ILBM.png | - |
| HI_GS_A1 | building | HI_GS_A1_BODEN3.ILBM.png, HI_GS_A1_BODEN4.ILBM.png, HI_GS_A1_TAERROBO.ILBM.png | - |
| HIxGS_A1 | building | HIxGS_A1_BODEN3.ILBM.png, HIxGS_A1_BODEN4.ILBM.png | - |
| HI_GS2OW | building | HI_GS2OW_HYPE.ILBM.png, HI_GS2OW_TAERROBO.ILBM.png | - |
| HIxGS2OW | building | HIxGS2OW_HYPE.ILBM.png | - |
| HI_FELD1 | building | HI_FELD1_BODEN3.ILBM.png, HI_FELD1_FCITY1.ILBM.png, HI_FELD1_FHUBI.ILBM.png | - |
| HIyFELD1 | building | HIyFELD1_BODEN3.ILBM.png, HIyFELD1_FHUBI.ILBM.png | - |
| HI_SCHL4 | building | HI_SCHL4_BODEN1.ILBM.png, HI_SCHL4_BODEN3.ILBM.png | - |
| HI_SCHL5 | building | HI_SCHL5_BODEN1.ILBM.png, HI_SCHL5_BODEN3.ILBM.png | - |
| HI_SCHL6 | building | HI_SCHL6_BODEN1.ILBM.png, HI_SCHL6_BODEN3.ILBM.png | - |
| HI_HUKL4 | building | HI_HUKL4_BODEN1.ILBM.png, HI_HUKL4_BODEN3.ILBM.png | - |
| HI_KMPKT | building | HI_KMPKT_BODEN2.ILBM.png | - |
| HI_RIES1 | building | HI_RIES1_BODEN3.ILBM.png, HI_RIES1_TAERROBO.ILBM.png | - |
| HIxRIES1 | building | HIxRIES1_BODEN3.ILBM.png, HIxRIES1_TAERROBO.ILBM.png | - |
| HI_RIES2 | building | HI_RIES2_BODEN3.ILBM.png, HI_RIES2_TAERROBO.ILBM.png | - |
| HIxRIES2 | building | HIxRIES2_BODEN3.ILBM.png, HIxRIES2_TAERROBO.ILBM.png | - |
| HI_RIES3 | building | HI_RIES3_BODEN3.ILBM.png, HI_RIES3_TAERROBO.ILBM.png | - |
| HIxRIES3 | building | HIxRIES3_BODEN3.ILBM.png, HIxRIES3_TAERROBO.ILBM.png | - |
| HI_RIES0 | building | HI_RIES0_BODEN3.ILBM.png, HI_RIES0_TAERROBO.ILBM.png | - |
| HIxRIES0 | building | HIxRIES0_BODEN3.ILBM.png, HIxRIES0_TAERROBO.ILBM.png | - |
| HIyRIES0 | building | HIyRIES0_BODEN3.ILBM.png, HIyRIES0_TAERROBO.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| HI_GR_1 | building | HI_GR_1_BODEN2.ILBM.png, HI_GR_1_TAERROBO.ILBM.png | - |
| HI_GR_2 | building | HI_GR_2_BODEN2.ILBM.png | - |
| HIxGR_1 | building | HIxGR_1_BODEN2.ILBM.png | - |
| HIzGR_1 | building | HIzGR_1_BODEN4.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| HI_TAERK | building | HI_TAERK_BODEN3.ILBM.png, HI_TAERK_TAERROBO.ILBM.png | - |
| HIXTAERK | building | HIXTAERK_BODEN3.ILBM.png, HIXTAERK_FAERROBO.ILBM.png, HIXTAERK_TAERROBO.ILBM.png | - |
| GS_NSTR0 | building | GS_NSTR0_BODEN3.ILBM.png, GS_NSTR0_HYPE.ILBM.png | - |
| GS_NSTR1 | building | GS_NSTR1_BODEN3.ILBM.png, GS_NSTR1_HYPE.ILBM.png | - |
| GS_NSTR2 | building | GS_NSTR2_BODEN3.ILBM.png, GS_NSTR2_HYPE.ILBM.png | - |
| GS_NSTR3 | building | GS_NSTR3_BODEN3.ILBM.png, GS_NSTR3_HYPE.ILBM.png | - |
| GS_BAUR2 | building | GS_BAUR2_BODEN3.ILBM.png, GS_BAUR2_TAERROBO.ILBM.png | - |
| GSxBAUR2 | building | GSxBAUR2_BODEN3.ILBM.png, GSxBAUR2_FAERROBO.ILBM.png | - |
| GSyBAUR2 | building | GSyBAUR2_BODEN3.ILBM.png, GSyBAUR2_FAERROBO.ILBM.png | - |
| GSzBAUR2 | building | GSzBAUR2_BODEN3.ILBM.png | - |
| GS_BAUR3 | building | GS_BAUR3_BODEN3.ILBM.png, GS_BAUR3_TAERROBO.ILBM.png | - |
| GSxBAUR3 | building | GSxBAUR3_BODEN3.ILBM.png, GSxBAUR3_FAERROBO.ILBM.png | - |
| GSyBAUR3 | building | GSyBAUR3_BODEN3.ILBM.png, GSyBAUR3_FAERROBO.ILBM.png | - |
| GSzBAUR3 | building | GSzBAUR3_BODEN3.ILBM.png | - |
| GS_NSTR4 | building | GS_NSTR4_BODEN4.ILBM.png, GS_NSTR4_HYPE.ILBM.png | - |
| GS_NSTR5 | building | GS_NSTR5_BODEN4.ILBM.png, GS_NSTR5_HYPE.ILBM.png | - |
| GS_NSTR6 | building | GS_NSTR6_BODEN4.ILBM.png, GS_NSTR6_HYPE.ILBM.png | - |
| GS_NSTR7 | building | GS_NSTR7_BODEN3.ILBM.png, GS_NSTR7_BODEN4.ILBM.png, GS_NSTR7_HYPE.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| GS_DHNEU | building | GS_DHNEU_BERUD.ILBM.png, GS_DHNEU_BODEN3.ILBM.png, GS_DHNEU_CITY1.ILBM.png | - |
| GSxDHNEU | building | GSxDHNEU_BODEN3.ILBM.png, GSxDHNEU_FBERUD.ILBM.png, GSxDHNEU_FCITY1.ILBM.png | - |
| GSyDHNEU | building | GSyDHNEU_BODEN3.ILBM.png, GSyDHNEU_FBERUD.ILBM.png, GSyDHNEU_FCITY1.ILBM.png | - |
| GSzDHNEU | building | GSzDHNEU_BODEN4.ILBM.png | - |
| HI_BERGA | building | HI_BERGA_BODEN3.ILBM.png | - |
| HI_BERGB | building | HI_BERGB_BODEN3.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| HI_MACHT | building | HI_MACHT_BERUD.ILBM.png, HI_MACHT_BODEN2.ILBM.png, HI_MACHT_MACHT.ILBM.png | - |
| HIxMACHT | building | HIxMACHT_BODEN2.ILBM.png, HIxMACHT_FBERUD.ILBM.png, HIxMACHT_FMACHT.ILBM.png | - |
| HIyMACHT | building | HIyMACHT_BODEN2.ILBM.png, HIyMACHT_FBERUD.ILBM.png, HIyMACHT_FMACHT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| GS_TOR | building | GS_TOR_BODEN3.ILBM.png, GS_TOR_TAERROBO.ILBM.png | - |
| GSxTOR | building | GSxTOR_BODEN3.ILBM.png, GSxTOR_FAERROBO.ILBM.png | - |
| GSyTOR | building | GSyTOR_BODEN3.ILBM.png, GSyTOR_FAERROBO.ILBM.png | - |
| GSzTOR | building | GSzTOR_BODEN3.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| HIzHUKL1 | building | HIzHUKL1_BODEN3.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| GS_LUUCH | building | GS_LUUCH_BODEN4.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| GS_SCHL3 | building | GS_SCHL3_BODEN1.ILBM.png, GS_SCHL3_BODEN3.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| GS_BERG1 | building | GS_BERG1_BODEN3.ILBM.png, GS_BERG1_BODEN4.ILBM.png | - |
| GS_BERG2 | building | GS_BERG2_BODEN3.ILBM.png, GS_BERG2_BODEN4.ILBM.png | - |
| GS_STRE | building | GS_STRE_HYPE.ILBM.png | - |
| GS_STREA | building | GS_STREA_BODEN3.ILBM.png, GS_STREA_BODEN4.ILBM.png | - |
| GS_STREB | building | GS_STREB_BODEN3.ILBM.png, GS_STREB_BODEN4.ILBM.png | - |
| GS_STREC | building | GS_STREC_BODEN3.ILBM.png, GS_STREC_BODEN4.ILBM.png | - |
| GS_STRED | building | GS_STRED_HYPE.ILBM.png | - |
| GS_STREE | building | GS_STREE_BODEN4.ILBM.png, GS_STREE_HYPE.ILBM.png | - |
| GS_STREF | building | GS_STREF_BODEN4.ILBM.png, GS_STREF_HYPE.ILBM.png | - |
| GS_STREz | building | GS_STREz_BODEN4.ILBM.png, GS_STREz_FHUBI.ILBM.png, GS_STREz_HYPE.ILBM.png | - |
| GSxSTREz | building | GSxSTREz_BODEN4.ILBM.png, GSxSTREz_FHUBI.ILBM.png, GSxSTREz_HYPE.ILBM.png | - |
| GSzSTREz | building | GSzSTREz_BODEN4.ILBM.png, GSzSTREz_HYPE.ILBM.png | - |
| GS_SCHL1 | building | GS_SCHL1_BODEN1.ILBM.png, GS_SCHL1_BODEN3.ILBM.png | - |
| GS_SCHL2 | building | GS_SCHL2_BODEN1.ILBM.png, GS_SCHL2_BODEN3.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set3_xp (dataxp/Set3)

### set3_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 163 | 150 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 97 | 0 | 85 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 40 | 40 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| faerrobo.ilbm | 30 | 27 | 3 | 0 | 0 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 270; models with meshes: 625; empty models: 43.

### set3_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set4_xp (dataxp/Set4)

### set4_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 163 | 150 | 13 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 98 | 0 | 86 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 58 | 33 | 25 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 40 | 40 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 35 | 0 | 3 | 32 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| faerrobo.ilbm | 30 | 27 | 3 | 0 | 0 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| taerrobo.ilbm | 15 | 7 | 8 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 267; models with meshes: 627; empty models: 43.

### set4_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ET_EMPTY | building | ET_EMPTY_BODEN2.ILBM.png | - |
| ER_EMTPY | building | ER_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ET_CITY1 | building | ET_CITY1_BERUD.ILBM.png, ET_CITY1_BODEN2.ILBM.png, ET_CITY1_CITY1.ILBM.png | - |
| ETxCITY1 | building | ETxCITY1_BODEN2.ILBM.png, ETxCITY1_FBERUD.ILBM.png, ETxCITY1_FCITY1.ILBM.png | - |
| ETyCITY1 | building | ETyCITY1_BODEN2.ILBM.png, ETyCITY1_FBERUD.ILBM.png, ETyCITY1_FCITY1.ILBM.png | - |
| ETzCITYn | building | ETzCITYn_BODEN2.ILBM.png | - |
| ET_CITY2 | building | ET_CITY2_BERUD.ILBM.png, ET_CITY2_BODEN2.ILBM.png, ET_CITY2_CITY1.ILBM.png | - |
| ETxCITY2 | building | ETxCITY2_BODEN2.ILBM.png, ETxCITY2_FBERUD.ILBM.png, ETxCITY2_FCITY1.ILBM.png | - |
| ETyCITY2 | building | ETyCITY2_BODEN2.ILBM.png, ETyCITY2_FBERUD.ILBM.png, ETyCITY2_FCITY1.ILBM.png | - |
| ET_MUSE | building | ET_MUSE_BERUD.ILBM.png, ET_MUSE_BODEN2.ILBM.png, ET_MUSE_CITY1.ILBM.png | - |
| ETxMUSE | building | ETxMUSE_BODEN2.ILBM.png, ETxMUSE_FBERUD.ILBM.png, ETxMUSE_FCITY1.ILBM.png | - |
| ETyMUSE | building | ETyMUSE_BODEN2.ILBM.png, ETyMUSE_FBERUD.ILBM.png, ETyMUSE_FCITY1.ILBM.png | - |
| ETzMUSE | building | ETzMUSE_BODEN2.ILBM.png | - |
| ET_HO | building | ET_HO_BERUD.ILBM.png, ET_HO_BODEN2.ILBM.png, ET_HO_CITY1.ILBM.png | - |
| ETxHO | building | ETxHO_BODEN2.ILBM.png, ETxHO_FBERUD.ILBM.png, ETxHO_FCITY1.ILBM.png | - |
| ETyHO | building | ETyHO_BODEN2.ILBM.png, ETyHO_FBERUD.ILBM.png, ETyHO_FCITY1.ILBM.png | - |
| ETzHO | building | ETzHO_BODEN2.ILBM.png, ETzHO_FBERUD.ILBM.png, ETzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ET_KRATR | building | ET_KRATR_BODEN2.ILBM.png | - |
| ET_KRAT2 | building | ET_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| ER_FLECK | building | ER_FLECK_BODEN2.ILBM.png | - |
| ER_KRAT1 | building | ER_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| ET_SLUM1 | building | ET_SLUM1_BERUD.ILBM.png, ET_SLUM1_BODEN2.ILBM.png | - |
| ETxSLUM1 | building | ETxSLUM1_BODEN2.ILBM.png, ETxSLUM1_FBERUD.ILBM.png | - |
| EtySLUM1 | building | EtySLUM1_BODEN2.ILBM.png, EtySLUM1_FBERUD.ILBM.png | - |
| ER_SLUM1 | building | ER_SLUM1_BERUD.ILBM.png, ER_SLUM1_BODEN1.ILBM.png | - |
| ERxSLUM1 | building | ERxSLUM1_BODEN1.ILBM.png, ERxSLUM1_FBERUD.ILBM.png | - |
| ERySLUM1 | building | ERySLUM1_BODEN1.ILBM.png, ERySLUM1_FBERUD.ILBM.png | - |
| ER_SLUM3 | building | ER_SLUM3_BODEN1.ILBM.png, ER_SLUM3_SHRTTWND.ILBM.png | - |
| ERxSLUM3 | building | ERxSLUM3_BODEN1.ILBM.png, ERxSLUM3_FHRTTWND.ILBM.png | - |
| ERySLUM3 | building | ERySLUM3_BODEN1.ILBM.png, ERySLUM3_FHRTTWND.ILBM.png | - |
| ERzSLUM3 | building | ERzSLUM3_BODEN2.ILBM.png | - |
| ER_SLUM2 | building | ER_SLUM2_BERUD.ILBM.png, ER_SLUM2_BODEN1.ILBM.png | - |
| ERxSLUM2 | building | ERxSLUM2_BODEN1.ILBM.png, ERxSLUM2_FBERUD.ILBM.png | - |
| ERySLUM2 | building | ERySLUM2_BODEN1.ILBM.png, ERySLUM2_BODEN2.ILBM.png, ERySLUM2_FBERUD.ILBM.png | - |
| ERzSLUM2 | building | ERzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| ER_HUKKL | building | ER_HUKKL_BODEN1.ILBM.png | - |
| ER_SANFT | building | ER_SANFT_BODEN1.ILBM.png | - |
| ET_KMPKT | building | ET_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set5_xp (dataxp/Set5)

### set5_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 163 | 150 | 13 | 0 | 0 |
| boden2.ilbm | 109 | 0 | 101 | 8 | 0 |
| boden3.ilbm | 96 | 0 | 64 | 32 | 0 |
| boden1.ilbm | 86 | 0 | 74 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 59 | 33 | 26 | 0 | 0 |
| fhubi.ilbm | 55 | 41 | 14 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| air1txt.ilbm | 41 | 40 | 1 | 0 | 0 |
| boden4.ilbm | 38 | 0 | 38 | 0 | 0 |
| faerrobo.ilbm | 37 | 27 | 10 | 0 | 0 |
| hype.ilbm | 37 | 0 | 35 | 2 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| boden5.ilbm | 33 | 2 | 9 | 22 | 0 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| taerrobo.ilbm | 24 | 7 | 17 | 0 | 0 |
| fhype.ilbm | 24 | 2 | 22 | 0 | 0 |
| fberud.ilbm | 23 | 3 | 20 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| fmacht.ilbm | 19 | 10 | 9 | 0 | 0 |
| macht.ilbm | 12 | 0 | 12 | 0 | 0 |
| fcity1.ilbm | 11 | 0 | 11 | 0 | 0 |
| berud.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |
| hotshot2.anm | 9 | 9 | 0 | 0 | 9 |
| shrttwnd.ilbm | 8 | 4 | 4 | 0 | 0 |
| city1.ilbm | 7 | 2 | 5 | 0 | 0 |
| brgbltz.anm | 6 | 5 | 1 | 0 | 6 |

Distinct textures referenced: 262; models with meshes: 643; empty models: 43.

### set5_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | vehicle | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | vehicle | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | vehicle | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | vehicle | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | vehicle | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | vehicle | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | vehicle | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| WS_CITY2 | building | WS_CITY2_BERUD.ILBM.png, WS_CITY2_BODEN2.ILBM.png, WS_CITY2_CITY1.ILBM.png | - |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| WS_HO | building | WS_HO_BERUD.ILBM.png, WS_HO_BODEN2.ILBM.png, WS_HO_CITY1.ILBM.png | - |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| HI_GS2NS | building | HI_GS2NS_HYPE.ILBM.png | - |
| HIxGS_NS | building | HIxGS_NS_HYPE.ILBM.png | - |
| HI_GS_NS | building | HI_GS_NS_HYPE.ILBM.png, HI_GS_NS_TAERROBO.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| HI_GS2_1 | building | HI_GS2_1_BODEN3.ILBM.png | - |
| HI_GS2_2 | building | HI_GS2_2_BODEN3.ILBM.png | - |
| HI_FELD2 | building | HI_FELD2_AIR1TXT.ILBM.png, HI_FELD2_BODEN3.ILBM.png, HI_FELD2_FCITY1.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| HI_GS1_1 | building | HI_GS1_1_BODEN3.ILBM.png | - |
| HI_GS1_2 | building | HI_GS1_2_BODEN3.ILBM.png | - |
| HIYFELD2 | building | HIYFELD2_BODEN3.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| HI_HUKL1 | building | HI_HUKL1_BODEN3.ILBM.png | - |
| HI_HUKL2 | building | HI_HUKL2_BODEN3.ILBM.png | - |
| HI_HUKL3 | building | HI_HUKL3_BODEN1.ILBM.png, HI_HUKL3_BODEN3.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| GS_MONT1 | building | GS_MONT1_BODEN1.ILBM.png, GS_MONT1_BODEN3.ILBM.png | - |
| GS_MONT3 | building | GS_MONT3_BODEN3.ILBM.png | - |
| GS_MONT2 | building | GS_MONT2_BODEN3.ILBM.png | - |
| GS_MONT4 | building | GS_MONT4_BODEN3.ILBM.png | - |
| GS_MONT5 | building | GS_MONT5_BODEN1.ILBM.png, GS_MONT5_BODEN3.ILBM.png | - |
| GS_HUkl1 | building | GS_HUkl1_BODEN3.ILBM.png | - |
| GS_LOCH1 | building | GS_LOCH1_BODEN3.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| HI_BIG | building | HI_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| HI_GS_X | building | HI_GS_X_BODEN3.ILBM.png, HI_GS_X_BODEN4.ILBM.png | - |
| HI_GS_X2 | building | HI_GS_X2_BODEN3.ILBM.png, HI_GS_X2_BODEN4.ILBM.png | - |
| HI_GS_OW | building | HI_GS_OW_HYPE.ILBM.png, HI_GS_OW_TAERROBO.ILBM.png | - |
| HIxGS_OW | building | HIxGS_OW_HYPE.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| HI_GS_A | building | HI_GS_A_BODEN3.ILBM.png, HI_GS_A_BODEN4.ILBM.png | - |
| HI_GS_A1 | building | HI_GS_A1_BODEN3.ILBM.png, HI_GS_A1_BODEN4.ILBM.png, HI_GS_A1_TAERROBO.ILBM.png | - |
| HIxGS_A1 | building | HIxGS_A1_BODEN3.ILBM.png, HIxGS_A1_BODEN4.ILBM.png | - |
| HI_GS2OW | building | HI_GS2OW_HYPE.ILBM.png, HI_GS2OW_TAERROBO.ILBM.png | - |
| HIxGS2OW | building | HIxGS2OW_HYPE.ILBM.png | - |
| HI_FELD1 | building | HI_FELD1_BODEN3.ILBM.png, HI_FELD1_FCITY1.ILBM.png, HI_FELD1_FHUBI.ILBM.png | - |
| HIyFELD1 | building | HIyFELD1_BODEN3.ILBM.png, HIyFELD1_FHUBI.ILBM.png | - |
| HI_SCHL4 | building | HI_SCHL4_BODEN1.ILBM.png, HI_SCHL4_BODEN3.ILBM.png | - |
| HI_SCHL5 | building | HI_SCHL5_BODEN1.ILBM.png, HI_SCHL5_BODEN3.ILBM.png | - |
| HI_SCHL6 | building | HI_SCHL6_BODEN1.ILBM.png, HI_SCHL6_BODEN3.ILBM.png | - |
| HI_HUKL4 | building | HI_HUKL4_BODEN1.ILBM.png, HI_HUKL4_BODEN3.ILBM.png | - |
| HI_KMPKT | building | HI_KMPKT_BODEN2.ILBM.png | - |
| XX_OELP1 | building | XX_OELP1_BODEN1.ILBM.png, XX_OELP1_FHYPE.ILBM.png, XX_OELP1_MTL.ILBM.png | - |
| XXxOELP1 | building | XXxOELP1_BODEN1.ILBM.png, XXxOELP1_FHYPE.ILBM.png | - |
| WG_pyram | building | WG_pyram_HYPE.ILBM.png | - |
| WGxpyram | building | WGxpyram_HYPE.ILBM.png | - |
| WGypyram | building | WGypyram_HYPE.ILBM.png | - |
| WG_STELE | building | WG_STELE_BODEN1.ILBM.png, WG_STELE_MACHT.ILBM.png | - |
| WGxSTELE | building | WGxSTELE_BODEN1.ILBM.png, WGxSTELE_MACHT.ILBM.png | - |
| WGySTELE | building | WGySTELE_BODEN1.ILBM.png, WGySTELE_MACHT.ILBM.png | - |
| WG_SPHNX | building | WG_SPHNX_BODEN1.ILBM.png, WG_SPHNX_FHYPE.ILBM.png, WG_SPHNX_HYPE.ILBM.png | - |
| WGxSPHNX | building | WGxSPHNX_BODEN1.ILBM.png, WGxSPHNX_HYPE.ILBM.png | - |
| WGySPHNX | building | WGySPHNX_BODEN1.ILBM.png, WGySPHNX_HYPE.ILBM.png | - |
| WG_SMALL | building | WG_SMALL_HYPE.ILBM.png | - |
| WGxSMALL | building | WGxSMALL_HYPE.ILBM.png | - |
| WGySMALL | building | WGySMALL_HYPE.ILBM.png | - |
| HI_GR_1 | building | HI_GR_1_BODEN2.ILBM.png, HI_GR_1_TAERROBO.ILBM.png | - |
| HI_GR_2 | building | HI_GR_2_BODEN2.ILBM.png | - |
| HIxGR_1 | building | HIxGR_1_BODEN2.ILBM.png | - |
| HIzGR_1 | building | HIzGR_1_BODEN4.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| wg_tor | building | wg_tor_BODEN1.ILBM.png, wg_tor_HYPE.ILBM.png | - |
| wgxtor | building | wgxtor_BODEN1.ILBM.png, wgxtor_HYPE.ILBM.png | - |
| wgytor | building | wgytor_BODEN1.ILBM.png, wgytor_HYPE.ILBM.png | - |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| GS_BAUR2 | building | GS_BAUR2_BODEN3.ILBM.png, GS_BAUR2_TAERROBO.ILBM.png | - |
| GSxBAUR2 | building | GSxBAUR2_BODEN3.ILBM.png, GSxBAUR2_FAERROBO.ILBM.png | - |
| GSyBAUR2 | building | GSyBAUR2_BODEN3.ILBM.png, GSyBAUR2_FAERROBO.ILBM.png | - |
| GSzBAUR2 | building | GSzBAUR2_BODEN3.ILBM.png | - |
| GS_BAUR3 | building | GS_BAUR3_BODEN3.ILBM.png, GS_BAUR3_TAERROBO.ILBM.png | - |
| GSxBAUR3 | building | GSxBAUR3_BODEN3.ILBM.png, GSxBAUR3_FAERROBO.ILBM.png | - |
| GSyBAUR3 | building | GSyBAUR3_BODEN3.ILBM.png, GSyBAUR3_FAERROBO.ILBM.png | - |
| GSzBAUR3 | building | GSzBAUR3_BODEN3.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| HI_TAERK | building | HI_TAERK_BODEN3.ILBM.png, HI_TAERK_TAERROBO.ILBM.png | - |
| HIXTAERK | building | HIXTAERK_BODEN3.ILBM.png, HIXTAERK_FAERROBO.ILBM.png, HIXTAERK_TAERROBO.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| GS_DHNEU | building | GS_DHNEU_BERUD.ILBM.png, GS_DHNEU_BODEN3.ILBM.png, GS_DHNEU_CITY1.ILBM.png | - |
| GSxDHNEU | building | GSxDHNEU_BODEN3.ILBM.png, GSxDHNEU_FBERUD.ILBM.png, GSxDHNEU_FCITY1.ILBM.png | - |
| GSyDHNEU | building | GSyDHNEU_BODEN3.ILBM.png, GSyDHNEU_FBERUD.ILBM.png, GSyDHNEU_FCITY1.ILBM.png | - |
| GSzDHNEU | building | GSzDHNEU_BODEN4.ILBM.png | - |
| HIzHUKL1 | building | HIzHUKL1_BODEN3.ILBM.png | - |
| HI_BERGA | building | HI_BERGA_BODEN3.ILBM.png | - |
| HI_BERGB | building | HI_BERGB_BODEN3.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| HI_MACHT | building | HI_MACHT_BERUD.ILBM.png, HI_MACHT_BODEN2.ILBM.png, HI_MACHT_MACHT.ILBM.png | - |
| HIxMACHT | building | HIxMACHT_BODEN2.ILBM.png, HIxMACHT_FBERUD.ILBM.png, HIxMACHT_FMACHT.ILBM.png | - |
| HIyMACHT | building | HIyMACHT_BODEN2.ILBM.png, HIyMACHT_FBERUD.ILBM.png, HIyMACHT_FMACHT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| GS_TOR | building | GS_TOR_BODEN3.ILBM.png, GS_TOR_TAERROBO.ILBM.png | - |
| GSxTOR | building | GSxTOR_BODEN3.ILBM.png, GSxTOR_FAERROBO.ILBM.png | - |
| GSyTOR | building | GSyTOR_BODEN3.ILBM.png, GSyTOR_FAERROBO.ILBM.png | - |
| GSzTOR | building | GSzTOR_BODEN3.ILBM.png | - |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| GS_NSTR0 | building | GS_NSTR0_BODEN3.ILBM.png, GS_NSTR0_HYPE.ILBM.png | - |
| GS_NSTR1 | building | GS_NSTR1_BODEN3.ILBM.png, GS_NSTR1_HYPE.ILBM.png | - |
| GS_NSTR2 | building | GS_NSTR2_BODEN3.ILBM.png, GS_NSTR2_HYPE.ILBM.png | - |
| GS_NSTR3 | building | GS_NSTR3_BODEN3.ILBM.png, GS_NSTR3_HYPE.ILBM.png | - |
| GS_NSTR4 | building | GS_NSTR4_BODEN4.ILBM.png, GS_NSTR4_HYPE.ILBM.png | - |
| GS_NSTR5 | building | GS_NSTR5_BODEN4.ILBM.png, GS_NSTR5_HYPE.ILBM.png | - |
| GS_NSTR6 | building | GS_NSTR6_BODEN4.ILBM.png, GS_NSTR6_HYPE.ILBM.png | - |
| GS_NSTR7 | building | GS_NSTR7_BODEN3.ILBM.png, GS_NSTR7_BODEN4.ILBM.png, GS_NSTR7_HYPE.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| GS_LUUCH | building | GS_LUUCH_BODEN4.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| GS_SCHL3 | building | GS_SCHL3_BODEN1.ILBM.png, GS_SCHL3_BODEN3.ILBM.png | - |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| GS_BERG1 | building | GS_BERG1_BODEN3.ILBM.png, GS_BERG1_BODEN4.ILBM.png | - |
| GS_BERG2 | building | GS_BERG2_BODEN3.ILBM.png, GS_BERG2_BODEN4.ILBM.png | - |
| GS_STRE | building | GS_STRE_HYPE.ILBM.png | - |
| GS_STREA | building | GS_STREA_BODEN3.ILBM.png, GS_STREA_BODEN4.ILBM.png | - |
| GS_STREB | building | GS_STREB_BODEN3.ILBM.png, GS_STREB_BODEN4.ILBM.png | - |
| GS_STREC | building | GS_STREC_BODEN3.ILBM.png, GS_STREC_BODEN4.ILBM.png | - |
| GS_STRED | building | GS_STRED_HYPE.ILBM.png | - |
| GS_STREE | building | GS_STREE_BODEN4.ILBM.png, GS_STREE_HYPE.ILBM.png | - |
| GS_STREF | building | GS_STREF_BODEN4.ILBM.png, GS_STREF_HYPE.ILBM.png | - |
| GS_STREz | building | GS_STREz_BODEN4.ILBM.png, GS_STREz_FHUBI.ILBM.png, GS_STREz_HYPE.ILBM.png | - |
| GSxSTREz | building | GSxSTREz_BODEN4.ILBM.png, GSxSTREz_FHUBI.ILBM.png, GSxSTREz_HYPE.ILBM.png | - |
| GSzSTREz | building | GSzSTREz_BODEN4.ILBM.png, GSzSTREz_HYPE.ILBM.png | - |
| GS_SCHL1 | building | GS_SCHL1_BODEN1.ILBM.png, GS_SCHL1_BODEN3.ILBM.png | - |
| GS_SCHL2 | building | GS_SCHL2_BODEN1.ILBM.png, GS_SCHL2_BODEN3.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |

## set6_xp (dataxp/Set6)

### set6_xp: shared-atlas audit (models referencing each original texture)

| orig texture | models | vehicles | buildings | slurps | refs without per-model png |
|---|---|---|---|---|---|
| fx2.ilbm | 168 | 150 | 18 | 0 | 0 |
| boden2.ilbm | 156 | 0 | 148 | 8 | 0 |
| boden1.ilbm | 93 | 0 | 81 | 12 | 0 |
| fx1.ilbm | 77 | 76 | 1 | 0 | 0 |
| hubi.ilbm | 72 | 72 | 0 | 0 | 0 |
| mtl.ilbm | 60 | 33 | 27 | 0 | 0 |
| genes4-1.anm | 53 | 53 | 0 | 0 | 53 |
| fhubi.ilbm | 51 | 41 | 10 | 0 | 0 |
| bagger.ilbm | 47 | 44 | 3 | 0 | 0 |
| boden5.ilbm | 44 | 2 | 20 | 22 | 0 |
| air1txt.ilbm | 40 | 40 | 0 | 0 | 0 |
| fberud.ilbm | 37 | 3 | 34 | 0 | 0 |
| boden3.ilbm | 36 | 0 | 4 | 32 | 0 |
| genes3-1.anm | 33 | 33 | 0 | 0 | 33 |
| fbagger.ilbm | 32 | 32 | 0 | 0 | 0 |
| fmacht.ilbm | 32 | 10 | 22 | 0 | 0 |
| faerrobo.ilbm | 30 | 27 | 3 | 0 | 0 |
| boden4.ilbm | 29 | 0 | 29 | 0 | 0 |
| fhype.ilbm | 25 | 2 | 23 | 0 | 0 |
| berud.ilbm | 25 | 0 | 25 | 0 | 0 |
| macht.ilbm | 25 | 0 | 25 | 0 | 0 |
| fschrott.ilbm | 22 | 0 | 22 | 0 | 0 |
| hotshot1.anm | 19 | 19 | 0 | 0 | 19 |
| taerrobo.ilbm | 16 | 7 | 9 | 0 | 0 |
| fcity1.ilbm | 15 | 0 | 15 | 0 | 0 |
| shrttwnd.ilbm | 11 | 4 | 7 | 0 | 0 |
| city1.ilbm | 11 | 2 | 9 | 0 | 0 |
| fhrttwnd.ilbm | 11 | 0 | 11 | 0 | 0 |
| schrott.ilbm | 10 | 0 | 10 | 0 | 0 |
| prop1.anm | 9 | 9 | 0 | 0 | 9 |

Distinct textures referenced: 285; models with meshes: 636; empty models: 43.

### set6_xp: per-model textures

| model | group | per-model png files | pool-only (ANM atlas) textures |
|---|---|---|---|
| VP_BRGR1 | vehicle | VP_BRGR1_AIR1TXT.ILBM.png, VP_BRGR1_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR1 | vehicle | VPfBRGR1_AIR1TXT.ILBM.png, VPfBRGR1_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR1 | vehicle | VPdBRGR1_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR1 | vehicle | VPwBRGR1_AIR1TXT.ILBM.png | - |
| VPxBRGR1 | vehicle | VPxBRGR1_AIR1TXT.ILBM.png | - |
| VPgBRGR1 | vehicle | VPgBRGR1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BRGR2 | vehicle | VP_BRGR2_AIR1TXT.ILBM.png, VP_BRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPfBRGR2 | vehicle | VPfBRGR2_AIR1TXT.ILBM.png, VPfBRGR2_FX2.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png |
| VPdBRGR2 | vehicle | VPdBRGR2_FX2.ILBM.png | 16109602.ANM.png, 16109603.ANM.png, BRGBLTZ.ANM.png |
| VPwBRGR2 | vehicle | VPwBRGR2_AIR1TXT.ILBM.png | - |
| VPxBRGR2 | vehicle | VPxBRGR2_AIR1TXT.ILBM.png, VPxBRGR2_FX2.ILBM.png | 16109602.ANM.png, BRGBLTZ.ANM.png |
| VPgBRGR2 | vehicle | VPgBRGR2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_HUBI1 | vehicle | VP_HUBI1_FX2.ILBM.png, VP_HUBI1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI1 | vehicle | VPfHUBI1_FHUBI.ILBM.png, VPfHUBI1_FX2.ILBM.png, VPfHUBI1_HUBI.ILBM.png | FHUBI.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPdHUBI1 | vehicle | (empty model) | |
| VPwHUBI1 | vehicle | VPwHUBI1_FHUBI.ILBM.png, VPwHUBI1_HUBI.ILBM.png | - |
| VPxHUBI1 | vehicle | VPxHUBI1_FHUBI.ILBM.png, VPxHUBI1_HUBI.ILBM.png | - |
| VPgHUBI1 | vehicle | VPgHUBI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_PANZ1 | vehicle | VP_PANZ1_AIR1TXT.ILBM.png, VP_PANZ1_HUBI.ILBM.png | PANZERKETTEN.png |
| VPfPANZ1 | vehicle | VPfPANZ1_AIR1TXT.ILBM.png, VPfPANZ1_FX2.ILBM.png, VPfPANZ1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZERKETTEN.png |
| VPdPANZ1 | vehicle | (empty model) | |
| VPwPANZ1 | vehicle | VPwPANZ1_AIR1TXT.ILBM.png, VPwPANZ1_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ1 | vehicle | VPgPANZ1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_HUBI2 | vehicle | VP_HUBI2_BAGGER.ILBM.png, VP_HUBI2_FX2.ILBM.png, VP_HUBI2_HUBI.ILBM.png | PROP1.ANM.png |
| VPfHUBI2 | vehicle | VPfHUBI2_BAGGER.ILBM.png, VPfHUBI2_FHUBI.ILBM.png, VPfHUBI2_FX2.ILBM.png, VPfHUBI2_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, HUBI3.ANM.png, HUBI4.ANM.png, PROP1.ANM.png |
| VPdHUBI2 | vehicle | (empty model) | |
| VPwHUBI2 | vehicle | VPwHUBI2_BAGGER.ILBM.png, VPwHUBI2_HUBI.ILBM.png | - |
| VPxHUBI2 | vehicle | VPxHUBI2_BAGGER.ILBM.png | - |
| VPgHUBI2 | vehicle | VPgHUBI2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SIMPL | vehicle | VP_SIMPL_BAGGER.ILBM.png, VP_SIMPL_FBAGGER.ILBM.png | 01059701.ANM.png |
| VPfSIMPL | vehicle | VPfSIMPL_BAGGER.ILBM.png, VPfSIMPL_FBAGGER.ILBM.png, VPfSIMPL_FX2.ILBM.png | 01059701.ANM.png, 01059702.ANM.png, 01059703.ANM.png |
| dummy | building | (empty model) | |
| VPwSIMPL | vehicle | VPwSIMPL_BAGGER.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgSIMPL | vehicle | VPgSIMPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TAERO | vehicle | VP_TAERO_FX2.ILBM.png, VP_TAERO_TAERROBO.ILBM.png | BLITZL1.ANM.png, BLITZL2.ANM.png, BLITZL3.ANM.png, TAERINN.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| VP_FLAK2 | vehicle | VP_FLAK2_FHUBI.ILBM.png, VP_FLAK2_MTL.ILBM.png | - |
| VPfFLAK2 | vehicle | VPfFLAK2_FHUBI.ILBM.png, VPfFLAK2_FX2.ILBM.png, VPfFLAK2_MTL.ILBM.png | FLAK1.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_SATT1 | vehicle | VP_SATT1_BAGGER.ILBM.png | SATT.ANM.png |
| dummy | building | (empty model) | |
| VPdSATT1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxSATT1 | vehicle | VPxSATT1_FBAGGER.ILBM.png | - |
| VPgSATT1 | vehicle | VPgSATT1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLSML | vehicle | VP_FLSML_BAGGER.ILBM.png, VP_FLSML_FBAGGER.ILBM.png | 1302970A.ANM.png |
| VPfFLSML | vehicle | VPfFLSML_BAGGER.ILBM.png, VPfFLSML_FBAGGER.ILBM.png, VPfFLSML_FX2.ILBM.png | 1302970B.ANM.png, HOTSHOT1.ANM.png |
| VPdFLSML | vehicle | (empty model) | |
| VPwFLSML | vehicle | VPwFLSML_BAGGER.ILBM.png | - |
| VPxFLSML | vehicle | VPxFLSML_FBAGGER.ILBM.png | - |
| VPgFLSML | vehicle | VPgFLSML_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLUG1 | vehicle | VP_FLUG1_FX2.ILBM.png, VP_FLUG1_HUBI.ILBM.png | PROP1.ANM.png |
| VPfFLUG1 | vehicle | VPfFLUG1_FX2.ILBM.png, VPfFLUG1_HUBI.ILBM.png | MGFEUJA1.ANM.png, PROP1.ANM.png |
| VPdFLUG1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPxFLUG1 | vehicle | VPxFLUG1_FHUBI.ILBM.png | - |
| VPgFLUG1 | vehicle | VPgFLUG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GLID1 | vehicle | VP_GLID1_AIR1TXT.ILBM.png, VP_GLID1_BAGGER.ILBM.png, VP_GLID1_FBAGGER.ILBM.png, VP_GLID1_FX2.ILBM.png | 1302970C.ANM.png, 1402970A.ANM.png |
| VPfGLID1 | vehicle | VPfGLID1_AIR1TXT.ILBM.png, VPfGLID1_BAGGER.ILBM.png, VPfGLID1_FBAGGER.ILBM.png, VPfGLID1_FX2.ILBM.png | 1302970C.ANM.png, 13059701.ANM.png, 13059702.ANM.png, 1402970A.ANM.png |
| VPdGLID1 | vehicle | (empty model) | |
| VPwGLID1 | vehicle | VPwGLID1_BAGGER.ILBM.png | - |
| VPxGLID1 | vehicle | VPxGLID1_FBAGGER.ILBM.png | - |
| VPgGLID1 | vehicle | VPgGLID1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_RAKT1 | vehicle | VP_RAKT1_HUBI.ILBM.png | - |
| OP_EXPL1 | vehicle | (empty model) | |
| VP_GRAN1 | vehicle | VP_GRAN1_FHUBI.ILBM.png, VP_GRAN1_HUBI.ILBM.png | 10039703.ANM.png |
| OP_EXPL3 | vehicle | (empty model) | |
| OP_EXPL2 | vehicle | (empty model) | |
| VP_JET1 | vehicle | VP_JET1_BAGGER.ILBM.png, VP_JET1_FBAGGER.ILBM.png, VP_JET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPdJET1 | vehicle | (empty model) | |
| VPgJET1 | vehicle | VPgJET1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwJET1 | vehicle | VPwJET1_BAGGER.ILBM.png | - |
| VPxJET1 | vehicle | VPxJET1_BAGGER.ILBM.png, VPxJET1_FBAGGER.ILBM.png | - |
| VPfJET1 | vehicle | VPfJET1_BAGGER.ILBM.png, VPfJET1_FBAGGER.ILBM.png, VPfJET1_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VP_GLID2 | vehicle | VP_GLID2_FAERROBO.ILBM.png, VP_GLID2_FBAGGER.ILBM.png, VP_GLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPdGLID2 | vehicle | (empty model) | |
| VPgGLID2 | vehicle | VPgGLID2_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwGLID2 | vehicle | VPwGLID2_BAGGER.ILBM.png, VPwGLID2_FAERROBO.ILBM.png | - |
| VPxGLID2 | vehicle | VPxGLID2_FAERROBO.ILBM.png, VPxGLID2_FBAGGER.ILBM.png, VPxGLID2_FX1.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 29119602.ANM.png |
| VPfGLID2 | vehicle | VPfGLID2_FAERROBO.ILBM.png, VPfGLID2_FBAGGER.ILBM.png, VPfGLID2_FX1.ILBM.png, VPfGLID2_FX2.ILBM.png | 01129601.ANM.png, 14029700.ANM.png, 28049701.ANM.png, 28049702.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png |
| VP_WASP | vehicle | VP_WASP_BAGGER.ILBM.png, VP_WASP_FX2.ILBM.png | 27099601.ANM.png |
| VPdWASP | vehicle | (empty model) | |
| VPgWASP | vehicle | VPgWASP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwWASP | vehicle | VPwWASP_BAGGER.ILBM.png | - |
| VPxWASP | vehicle | VPxWASP_BAGGER.ILBM.png, VPxWASP_FBAGGER.ILBM.png | - |
| VPfWASP | vehicle | VPfWASP_BAGGER.ILBM.png, VPfWASP_FX2.ILBM.png | 10039701.ANM.png, PROP1.ANM.png |
| VP_PANZ2 | vehicle | VP_PANZ2_AIR1TXT.ILBM.png, VP_PANZ2_BAGGER.ILBM.png, VP_PANZ2_FBAGGER.ILBM.png, VP_PANZ2_FHUBI.ILBM.png, VP_PANZ2_FMACHT.ILBM.png, VP_PANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019803.ANM.png, 28019804.ANM.png |
| VPdPANZ2 | vehicle | (empty model) | |
| VPfPANZ2 | vehicle | VPfPANZ2_AIR1TXT.ILBM.png, VPfPANZ2_BAGGER.ILBM.png, VPfPANZ2_FBAGGER.ILBM.png, VPfPANZ2_FHUBI.ILBM.png, VPfPANZ2_FMACHT.ILBM.png, VPfPANZ2_FX2.ILBM.png, VPfPANZ2_HUBI.ILBM.png | 28019800.ANM.png, 28019802.ANM.png, 28019804.ANM.png, 28019805.ANM.png |
| VPwPANZ2 | vehicle | VPwPANZ2_AIR1TXT.ILBM.png, VPwPANZ2_BAGGER.ILBM.png, VPwPANZ2_FBAGGER.ILBM.png, VPwPANZ2_FHUBI.ILBM.png, VPwPANZ2_FMACHT.ILBM.png, VPwPANZ2_HUBI.ILBM.png | - |
| dummy | building | (empty model) | |
| VPgPANZ2 | vehicle | VPgPANZ2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_FLAK1 | vehicle | VP_FLAK1_MTL.ILBM.png | - |
| VPfFLAK1 | vehicle | VPfFLAK1_FX2.ILBM.png, VPfFLAK1_MTL.ILBM.png | 10030704.ANM.png, 10030705.ANM.png, FLAK1.ANM.png |
| VPgFLAK1 | vehicle | VPgFLAK1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_RAKT2 | vehicle | VP_RAKT2_HUBI.ILBM.png | - |
| OP_EIN1 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VP_KPAN1 | vehicle | VP_KPAN1_FHUBI.ILBM.png, VP_KPAN1_HUBI.ILBM.png | KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPfKPAN1 | vehicle | VPfKPAN1_FHUBI.ILBM.png, VPfKPAN1_FX2.ILBM.png, VPfKPAN1_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, KYTFIRE1.ANM.png, KYTKETT1.ANM.png, KYTKETT2.ANM.png |
| VPwKPAN1 | vehicle | VPwKPAN1_FHUBI.ILBM.png, VPwKPAN1_HUBI.ILBM.png | - |
| VPgKPAN1 | vehicle | VPgKPAN1_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdKPAN1 | vehicle | (empty model) | |
| VP_HUBI3 | vehicle | VP_HUBI3_BAGGER.ILBM.png, VP_HUBI3_FMACHT.ILBM.png, VP_HUBI3_FX2.ILBM.png, VP_HUBI3_MTL.ILBM.png, VP_HUBI3_SHRTTWND.ILBM.png, VP_HUBI3_TAERROBO.ILBM.png | 06119701.ANM.png |
| VPdHUBI3 | vehicle | (empty model) | |
| VPfHUBI3 | vehicle | VPfHUBI3_BAGGER.ILBM.png, VPfHUBI3_FMACHT.ILBM.png, VPfHUBI3_FX2.ILBM.png, VPfHUBI3_MTL.ILBM.png, VPfHUBI3_SHRTTWND.ILBM.png, VPfHUBI3_TAERROBO.ILBM.png | 06119701.ANM.png, HOTSHOT1.ANM.png |
| VPwHUBI3 | vehicle | VPwHUBI3_BAGGER.ILBM.png, VPwHUBI3_FMACHT.ILBM.png, VPwHUBI3_MTL.ILBM.png, VPwHUBI3_SHRTTWND.ILBM.png, VPwHUBI3_TAERROBO.ILBM.png | - |
| VPxHUBI3 | vehicle | VPxHUBI3_BAGGER.ILBM.png, VPxHUBI3_FMACHT.ILBM.png, VPxHUBI3_MTL.ILBM.png, VPxHUBI3_SHRTTWND.ILBM.png, VPxHUBI3_TAERROBO.ILBM.png | - |
| VPgHUBI3 | vehicle | VPgHUBI3_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| OP_EXPL4 | vehicle | (empty model) | |
| VP_RAKT3 | vehicle | VP_RAKT3_HUBI.ILBM.png | - |
| VP_RAKT4 | vehicle | VP_RAKT4_FX2.ILBM.png, VP_RAKT4_HUBI.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_ROBO | vehicle | VP_ROBO_FHUBI.ILBM.png, VP_ROBO_MTL.ILBM.png | 17099601.ANM.png, 17099602.ANM.png, 17099603.ANM.png, 17099604.ANM.png, 17099605.ANM.png, 17099606.ANM.png |
| VP_GIGNT | vehicle | VP_GIGNT_AIR1TXT.ILBM.png, VP_GIGNT_FX1.ILBM.png, VP_GIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGNAT3.ANM.png, GIGNAT4.ANM.png |
| VPdGIGNT | vehicle | (empty model) | |
| VPfGIGNT | vehicle | VPfGIGNT_AIR1TXT.ILBM.png, VPfGIGNT_FX1.ILBM.png, VPfGIGNT_FX2.ILBM.png | 01129601.ANM.png, GIGANT1.ANM.png, GIGANT_5.ANM.png, GIGANT_6.ANM.png |
| VPwGIGNT | vehicle | VPwGIGNT_AIR1TXT.ILBM.png | - |
| VPxGIGNT | vehicle | VPxGIGNT_AIR1TXT.ILBM.png | - |
| VPgGIGNT | vehicle | VPgGIGNT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_LASR1 | vehicle | VP_LASR1_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEX | vehicle | (empty model) | |
| VP_LASR2 | vehicle | VP_LASR2_FX2.ILBM.png | LASER1.ANM.png, LASERN1.ANM.png |
| VP_LASEY | vehicle | (empty model) | |
| VP_KROBO | vehicle | VP_KROBO_FHUBI.ILBM.png, VP_KROBO_HUBI.ILBM.png | KYROINN1.ANM.png, KYROINN2.ANM.png, KYROINN3.ANM.png |
| VP_BRGRO | vehicle | VP_BRGRO_AIR1TXT.ILBM.png, VP_BRGRO_FX2.ILBM.png | 20059801.ANM.png, 20059802.ANM.png, 20059803.ANM.png, 20059804.ANM.png, 20059806.ANM.png, 20059807.ANM.png, 20059808.ANM.png, 20059809.ANM.png, 2005980A.ANM.png, 2005980B.ANM.png, 2005980C.ANM.png, 2005980D.ANM.png, 2005980E.ANM.png, 2005980F.ANM.png, 2005980G.ANM.png, 2005980H.ANM.png |
| dummy | building | (empty model) | |
| VPdBRGRO | vehicle | (empty model) | |
| VP_GHTT | vehicle | (empty model) | |
| VP_KLEIN | vehicle | VP_KLEIN_FHYPE.ILBM.png | - |
| VP_MITTL | vehicle | VP_MITTL_FHYPE.ILBM.png | - |
| VP_LFLAK | vehicle | VP_LFLAK_FHUBI.ILBM.png, VP_LFLAK_FX2.ILBM.png, VP_LFLAK_MTL.ILBM.png | UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VPfLFLAK | vehicle | VPfLFLAK_FHUBI.ILBM.png, VPfLFLAK_FX2.ILBM.png, VPfLFLAK_MTL.ILBM.png | 0103970A.ANM.png, FLAK1.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png |
| VP_MFLAK | vehicle | VP_MFLAK_FHUBI.ILBM.png, VP_MFLAK_MTL.ILBM.png | - |
| VPfMFLAK | vehicle | VPfMFLAK_FHUBI.ILBM.png, VPfMFLAK_FX2.ILBM.png, VPfMFLAK_MTL.ILBM.png | HOTSHOT1.ANM.png |
| VPx | vehicle | (empty model) | |
| VP_GLOW | vehicle | VP_GLOW_FX2.ILBM.png | 18079601.ANM.png |
| VP_Xnew1 | vehicle | (empty model) | |
| VP_Xnew2 | vehicle | (empty model) | |
| VP_Xnew3 | vehicle | (empty model) | |
| VP_SULG1 | vehicle | VP_SULG1_FBAGGER.ILBM.png, VP_SULG1_FX1.ILBM.png | - |
| VPxSULG1 | vehicle | (empty model) | |
| VP_GRUEN | vehicle | VP_GRUEN_FX1.ILBM.png | 2507960A.ANM.png |
| VP_XGRUN | vehicle | (empty model) | |
| VP_PANZ3 | vehicle | VP_PANZ3_BAGGER.ILBM.png, VP_PANZ3_FBAGGER.ILBM.png, VP_PANZ3_FHUBI.ILBM.png, VP_PANZ3_HUBI.ILBM.png | PANZ2.ANM.png, PANZERKETTEN.png |
| VPfPANZ3 | vehicle | VPfPANZ3_BAGGER.ILBM.png, VPfPANZ3_FBAGGER.ILBM.png, VPfPANZ3_FHUBI.ILBM.png, VPfPANZ3_FX2.ILBM.png, VPfPANZ3_HUBI.ILBM.png | HOTSHOT1.ANM.png, HOTSHOT2.ANM.png, PANZ2.ANM.png, PANZERKETTEN.png |
| VPwPANZ3 | vehicle | VPwPANZ3_BAGGER.ILBM.png, VPwPANZ3_FHUBI.ILBM.png, VPwPANZ3_HUBI.ILBM.png | - |
| VPgPANZ3 | vehicle | VPgPANZ3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdPANZ3 | vehicle | (empty model) | |
| VP_RADA | vehicle | VP_RADA_FHUBI.ILBM.png, VP_RADA_MTL.ILBM.png | - |
| VPgRADA | vehicle | VPgRADA_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_SATT2 | vehicle | VP_SATT2_AIR1TXT.ILBM.png, VP_SATT2_FAERROBO.ILBM.png, VP_SATT2_FBAGGER.ILBM.png, VP_SATT2_FX1.ILBM.png | 25049701.ANM.png, 30049701.ANM.png |
| VPdSATT2 | vehicle | (empty model) | |
| VPxSATT2 | vehicle | VPxSATT2_FAERROBO.ILBM.png, VPxSATT2_FBAGGER.ILBM.png | 25049701.ANM.png |
| VPgSATT2 | vehicle | VPgSATT2_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BLUSH | vehicle | VP_BLUSH_FX2.ILBM.png | 21099601.ANM.png, 21099602.ANM.png, 21099603.ANM.png, 21099604.ANM.png |
| VP_RT | vehicle | VP_RT_BAGGER.ILBM.png, VP_RT_FBAGGER.ILBM.png, VP_RT_HUBI.ILBM.png | 3004970A.ANM.png, 3004970B.ANM.png, 3040970B.ANM.png |
| VPgRT | vehicle | VPgRT_FX2.ILBM.png | GENES4-1.ANM.png |
| VPdRT | vehicle | (empty model) | |
| VP_RTX | vehicle | VP_RTX_HUBI.ILBM.png | GRANATE.ANM.png |
| VPwRT | vehicle | VPwRT_BAGGER.ILBM.png, VPwRT_FBAGGER.ILBM.png, VPwRT_HUBI.ILBM.png | - |
| VP_TFLUG | vehicle | VP_TFLUG_FAERROBO.ILBM.png, VP_TFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png |
| VPfTFLUG | vehicle | VPfTFLUG_FAERROBO.ILBM.png, VPfTFLUG_FX2.ILBM.png | 30099601.ANM.png, 30099602.ANM.png, HOTSHOT1.ANM.png |
| VPwTFLUG | vehicle | VPwTFLUG_FAERROBO.ILBM.png | - |
| VPxTFLUG | vehicle | VPxTFLUG_FAERROBO.ILBM.png | - |
| VPdTFLUG | vehicle | (empty model) | |
| VPgTFLUG | vehicle | VPgTFLUG_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BUGGY | vehicle | VP_BUGGY_BAGGER.ILBM.png, VP_BUGGY_FHUBI.ILBM.png, VP_BUGGY_TAERROBO.ILBM.png | - |
| VPfBUGGY | vehicle | VPfBUGGY_BAGGER.ILBM.png, VPfBUGGY_FHUBI.ILBM.png, VPfBUGGY_FX2.ILBM.png, VPfBUGGY_TAERROBO.ILBM.png | HOTSHOT1.ANM.png |
| dummy | building | (empty model) | |
| VPgBUGGY | vehicle | VPgBUGGY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_BOMBA | vehicle | VP_BOMBA_BAGGER.ILBM.png, VP_BOMBA_FBAGGER.ILBM.png, VP_BOMBA_FX2.ILBM.png | 2002970A.ANM.png, 2002970B.ANM.png, 2002970C.ANM.png |
| VPxBOMBA | vehicle | VPxBOMBA_BAGGER.ILBM.png, VPxBOMBA_FBAGGER.ILBM.png | SMPLFEUA.ANM.png |
| VPgBOMBA | vehicle | VPgBOMBA_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPwBOMBA | vehicle | VPwBOMBA_BAGGER.ILBM.png | - |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPfSULG2 | vehicle | VPfSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPwSULG2 | vehicle | VPwSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPxSULG2 | vehicle | VPxSULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPdSULG2 | vehicle | (empty model) | |
| VPgSULG2 | vehicle | VPgSULG2_FX2.ILBM.png | GENES3-1.ANM.png |
| Vp_MFLSH | vehicle | Vp_MFLSH_FX2.ILBM.png | 1210960A.ANM.png, 1210960B.ANM.png, 1210960C.ANM.png |
| VP_BRGR3 | vehicle | VP_BRGR3_AIR1TXT.ILBM.png, VP_BRGR3_FX2.ILBM.png | 16109601.ANM.png, 16109602.ANM.png |
| VPDBRGR3 | vehicle | (empty model) | |
| dummy | building | (empty model) | |
| VPWBRGR3 | vehicle | VPWBRGR3_AIR1TXT.ILBM.png | - |
| VPXBRGR3 | vehicle | VPXBRGR3_AIR1TXT.ILBM.png | - |
| VPXBSHOT | vehicle | (empty model) | |
| VP_BSHOT | vehicle | VP_BSHOT_FX2.ILBM.png | - |
| OP_EIN2 | vehicle | (empty model) | |
| VP_X2 | vehicle | (empty model) | |
| VP_HILLB | vehicle | VP_HILLB_FBERUD.ILBM.png | - |
| VP_KYTIE | vehicle | VP_KYTIE_FBERUD.ILBM.png | - |
| VP_STCKN | vehicle | VP_STCKN_FBERUD.ILBM.png | - |
| VP_D_AUS | vehicle | (empty model) | |
| VP_KSATT | vehicle | VP_KSATT_FHUBI.ILBM.png, VP_KSATT_HUBI.ILBM.png | - |
| VPxKSATT | vehicle | VPxKSATT_HUBI.ILBM.png | - |
| VPgKSATT | vehicle | VPgKSATT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BRGR4 | vehicle | VP_BRGR4_AIR1TXT.ILBM.png | - |
| VP_TSERP | vehicle | VP_TSERP_AIR1TXT.ILBM.png, VP_TSERP_FBAGGER.ILBM.png, VP_TSERP_FX1.ILBM.png, VP_TSERP_MTL.ILBM.png | 01129601.ANM.png, 29119601.ANM.png, 29119602.ANM.png |
| VPxTSERP | vehicle | VPxTSERP_FBAGGER.ILBM.png, VPxTSERP_MTL.ILBM.png | - |
| VPgTSERP | vehicle | VPgTSERP_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_JUBEL | vehicle | (empty model) | |
| VPwTSERP | vehicle | VPwTSERP_AIR1TXT.ILBM.png, VPwTSERP_FBAGGER.ILBM.png, VPwTSERP_MTL.ILBM.png | - |
| VP_XPILZ | vehicle | (empty model) | |
| VP_MORSR | vehicle | VP_MORSR_MTL.ILBM.png | - |
| VPFMORSR | vehicle | VPFMORSR_MTL.ILBM.png | 07029701.ANM.png |
| VP_NFOX | vehicle | VP_NFOX_AIR1TXT.ILBM.png, VP_NFOX_BAGGER.ILBM.png, VP_NFOX_FHUBI.ILBM.png, VP_NFOX_FMACHT.ILBM.png, VP_NFOX_HUBI.ILBM.png, VP_NFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png |
| VPwNFOX | vehicle | VPwNFOX_AIR1TXT.ILBM.png, VPwNFOX_BAGGER.ILBM.png, VPwNFOX_FHUBI.ILBM.png, VPwNFOX_FMACHT.ILBM.png, VPwNFOX_HUBI.ILBM.png, VPwNFOX_MTL.ILBM.png | - |
| VPfNFOX | vehicle | VPfNFOX_AIR1TXT.ILBM.png, VPfNFOX_BAGGER.ILBM.png, VPfNFOX_FHUBI.ILBM.png, VPfNFOX_FMACHT.ILBM.png, VPfNFOX_FX2.ILBM.png, VPfNFOX_HUBI.ILBM.png, VPfNFOX_MTL.ILBM.png | 12099701.ANM.png, 12099702.ANM.png, 12099703.ANM.png, 12099707.ANM.png, 12099708.ANM.png, 1209970A.ANM.png, HOTSHOT1.ANM.png |
| VP_SULG5 | vehicle | VP_SULG5_FBAGGER.ILBM.png, VP_SULG5_FX1.ILBM.png | - |
| VP_SULX1 | vehicle | VP_SULX1_FX1.ILBM.png | - |
| VP_PANZ4 | vehicle | VP_PANZ4_FAERROBO.ILBM.png, VP_PANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png |
| VPwPANZ4 | vehicle | VPwPANZ4_FAERROBO.ILBM.png, VPwPANZ4_HUBI.ILBM.png | - |
| VPfPANZ4 | vehicle | VPfPANZ4_FAERROBO.ILBM.png, VPfPANZ4_FX2.ILBM.png, VPfPANZ4_HUBI.ILBM.png | 19029701.ANM.png, 19029702.ANM.png, 20029701.ANM.png, 20029702.ANM.png, HOTSHOT1.ANM.png |
| VPgPANZ4 | vehicle | VPgPANZ4_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MIG | vehicle | VP_MIG_FX1.ILBM.png, VP_MIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png |
| VPfMIG | vehicle | VPfMIG_FX1.ILBM.png, VPfMIG_FX2.ILBM.png, VPfMIG_HUBI.ILBM.png | 26029701.ANM.png, 29119602.ANM.png, HOTSHOT1.ANM.png, HOTSHOT2.ANM.png |
| VPwMIG | vehicle | VPwMIG_HUBI.ILBM.png | - |
| VPxMIG | vehicle | VPxMIG_FHUBI.ILBM.png | - |
| VPgMIG | vehicle | VPgMIG_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_BSECT | vehicle | VP_BSECT_FX2.ILBM.png, VP_BSECT_ROBONEU.ILBM.png | ROBOADD1.ANM.png, ROBOS1.ANM.png, UROBOFL1.ANM.png, UROBOFL2.ANM.png, UROBOL1.ANM.png, UROBOL1B.ANM.png, UROBOL2.ANM.png, UROBOL2B.ANM.png |
| VP_RAKT5 | vehicle | VP_RAKT5_HUBI.ILBM.png | - |
| OP_R3__1 | vehicle | OP_R3__1_FX1.ILBM.png | - |
| OP_R3__2 | vehicle | OP_R3__2_FX1.ILBM.png | - |
| OP_R3__3 | vehicle | OP_R3__3_FX1.ILBM.png | - |
| OP_RING4 | vehicle | OP_RING4_FX2.ILBM.png | 22049701.ANM.png, 22049702.ANM.png |
| OP_R___1 | vehicle | OP_R___1_FX2.ILBM.png | - |
| OP_R___2 | vehicle | OP_R___2_FX2.ILBM.png | - |
| OP_R___3 | vehicle | OP_R___3_FX2.ILBM.png | - |
| OP_R___4 | vehicle | OP_R___4_FX2.ILBM.png | - |
| OP_R___5 | vehicle | OP_R___5_FX2.ILBM.png | - |
| OP_R___6 | vehicle | OP_R___6_FX2.ILBM.png | - |
| OP_R___7 | vehicle | OP_R___7_FX2.ILBM.png | - |
| VP_SPEDY | vehicle | VP_SPEDY_FX1.ILBM.png, VP_SPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png |
| VPwSPEDY | vehicle | VPwSPEDY_HUBI.ILBM.png | - |
| VPfSPEDY | vehicle | VPfSPEDY_FX1.ILBM.png, VPfSPEDY_FX2.ILBM.png, VPfSPEDY_HUBI.ILBM.png | 26069701.ANM.png, 26069702.ANM.png, HOTSHOT1.ANM.png |
| VPgSPEDY | vehicle | VPgSPEDY_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_KUFO | vehicle | VP_KUFO_FX1.ILBM.png, VP_KUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VPwKUFO | vehicle | VPwKUFO_HUBI.ILBM.png | - |
| VPfKUFO | vehicle | VPfKUFO_FX1.ILBM.png, VPfKUFO_HUBI.ILBM.png | 260697AA.ANM.png |
| VP_SATT3 | vehicle | VP_SATT3_AIR1TXT.ILBM.png, VP_SATT3_FAERROBO.ILBM.png | - |
| VP_LSRED | vehicle | VP_LSRED_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_LSRE2 | vehicle | VP_LSRE2_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_REDIN | vehicle | VP_REDIN_FX1.ILBM.png | 25099701.ANM.png |
| VP_LSRE3 | vehicle | VP_LSRE3_FX1.ILBM.png | 03079701.ANM.png, 03079702.ANM.png |
| VP_ZEPPL | vehicle | VP_ZEPPL_FAERROBO.ILBM.png, VP_ZEPPL_FX1.ILBM.png, VP_ZEPPL_MTL.ILBM.png | 10079701.ANM.png, 10079702.ANM.png, 10079703.ANM.png, 10079704.ANM.png |
| VPgZEPPL | vehicle | VPgZEPPL_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxZEPPL | vehicle | (empty model) | |
| VP_MYKO1 | vehicle | VP_MYKO1_AIR1TXT.ILBM.png, VP_MYKO1_FX1.ILBM.png, VP_MYKO1_FX2.ILBM.png | 12079703.ANM.png, 12079704.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 1207970F.ANM.png |
| VPgMYKO1 | vehicle | VPgMYKO1_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_MYKO3 | vehicle | VP_MYKO3_AIR1TXT.ILBM.png, VP_MYKO3_FX1.ILBM.png, VP_MYKO3_FX2.ILBM.png | 1207970A.ANM.png, 1207970B.ANM.png, 1207970C.ANM.png, 1207970D.ANM.png, 1207970E.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| OP_HHK1 | vehicle | OP_HHK1_FX1.ILBM.png | - |
| OP_HHK2 | vehicle | OP_HHK2_FX1.ILBM.png | - |
| OP_HHK3 | vehicle | OP_HHK3_FX1.ILBM.png | - |
| OP_HHK4 | vehicle | OP_HHK4_FX1.ILBM.png | - |
| OP_HHK5 | vehicle | OP_HHK5_FX1.ILBM.png | - |
| OP_HHK6 | vehicle | OP_HHK6_FX1.ILBM.png | - |
| OP_HHK7 | vehicle | OP_HHK7_FX1.ILBM.png | - |
| OP_HK1 | vehicle | OP_HK1_FX1.ILBM.png | - |
| OP_HK2 | vehicle | OP_HK2_FX1.ILBM.png | - |
| OP_HK3 | vehicle | OP_HK3_FX1.ILBM.png | - |
| OP_HK4 | vehicle | OP_HK4_FX1.ILBM.png | - |
| OP_HK5 | vehicle | OP_HK5_FX1.ILBM.png | - |
| OP_HK6 | vehicle | OP_HK6_FX1.ILBM.png | - |
| OP_HK7 | vehicle | OP_HK7_FX1.ILBM.png | - |
| VP_HUELS | vehicle | VP_HUELS_FX2.ILBM.png | 25089702.ANM.png |
| dummy | building | (empty model) | |
| VP_MYKO2 | vehicle | VP_MYKO2_AIR1TXT.ILBM.png, VP_MYKO2_FX1.ILBM.png, VP_MYKO2_FX2.ILBM.png | 1207970C.ANM.png, 12079711.ANM.png, 12079717.ANM.png, 12079718.ANM.png |
| VP_MYKO4 | vehicle | VP_MYKO4_AIR1TXT.ILBM.png, VP_MYKO4_FX1.ILBM.png, VP_MYKO4_FX2.ILBM.png | 12079701.ANM.png, 12079702.ANM.png, 12079703.ANM.png, 12079704.ANM.png, 12079705.ANM.png, 12079706.ANM.png, 12079707.ANM.png, 12079708.ANM.png, 1207970A.ANM.png, 1207970B.ANM.png, 12079711.ANM.png, 12079712.ANM.png, 12079713.ANM.png, 12079714.ANM.png, 12079715.ANM.png, 12079718.ANM.png |
| VP_HUBI4 | vehicle | VP_HUBI4_FHUBI.ILBM.png, VP_HUBI4_FX2.ILBM.png, VP_HUBI4_HUBI.ILBM.png | PROP1.ANM.png |
| VPgMYKO2 | vehicle | VPgMYKO2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO3 | vehicle | VPgMYKO3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgMYKO4 | vehicle | VPgMYKO4_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgBRGR3 | vehicle | VPgBRGR3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPGSATT3 | vehicle | VPGSATT3_FX2.ILBM.png | GENES4-1.ANM.png |
| VPwHUBI4 | vehicle | VPwHUBI4_FHUBI.ILBM.png, VPwHUBI4_HUBI.ILBM.png | - |
| VPfHUBI4 | vehicle | VPfHUBI4_FHUBI.ILBM.png, VPfHUBI4_FX2.ILBM.png, VPfHUBI4_HUBI.ILBM.png | HOTSHOT2.ANM.png, PROP1.ANM.png |
| VPgNFOX | vehicle | VPgNFOX_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_WOLK1 | vehicle | VP_WOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_WOLK2 | vehicle | VP_WOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_WOLK3 | vehicle | VP_WOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_RAKT6 | vehicle | VP_RAKT6_FX2.ILBM.png, VP_RAKT6_MTL.ILBM.png | RAK4FIRE.ANM.png, RAK4HINT.ANM.png |
| VP_GLIDW | vehicle | VP_GLIDW_BAGGER.ILBM.png, VP_GLIDW_FX2.ILBM.png, VP_GLIDW_MTL.ILBM.png | 2509970A.ANM.png, 2509970B.ANM.png |
| VP_XOLK1 | vehicle | VP_XOLK1_FX1.ILBM.png | 23099701.ANM.png |
| VP_XOLK2 | vehicle | VP_XOLK2_FX1.ILBM.png | 23099702.ANM.png |
| VP_XOLK3 | vehicle | VP_XOLK3_FX1.ILBM.png | 23099703.ANM.png |
| VP_SMAL1 | vehicle | VP_SMAL1_FX1.ILBM.png | - |
| VP_SMAL2 | vehicle | VP_SMAL2_FX1.ILBM.png | - |
| VP_SMAL3 | vehicle | VP_SMAL3_FX1.ILBM.png | - |
| VP_SMAL4 | vehicle | VP_SMAL4_FX1.ILBM.png | - |
| VP_HFLA1 | vehicle | VP_HFLA1_FX1.ILBM.png | 250997XX.ANM.png |
| VP_HFLA2 | vehicle | VP_HFLA2_FX1.ILBM.png | 250997XY.ANM.png |
| VP_HFLA3 | vehicle | VP_HFLA3_FX1.ILBM.png | 250997XZ.ANM.png |
| VP_HWOL1 | vehicle | VP_HWOL1_FX1.ILBM.png | - |
| VP_HWOL2 | vehicle | VP_HWOL2_FX1.ILBM.png | - |
| VP_HWOL3 | vehicle | VP_HWOL3_FX1.ILBM.png | - |
| VP_HWOL4 | vehicle | VP_HWOL4_FX1.ILBM.png | - |
| VP_DFLAK | vehicle | VP_DFLAK_MTL.ILBM.png | - |
| VPfDFLAK | vehicle | VPfDFLAK_MTL.ILBM.png | FLAK1.ANM.png |
| VP_GABEL | vehicle | VP_GABEL_AIR1TXT.ILBM.png | - |
| VPfGABEL | vehicle | VPfGABEL_AIR1TXT.ILBM.png, VPfGABEL_FX2.ILBM.png | 10109701.ANM.png |
| VP_XFLKK | vehicle | VP_XFLKK_MTL.ILBM.png | - |
| VPfXFLKK | vehicle | VPfXFLKK_MTL.ILBM.png | 14109701.ANM.png |
| VPgXFLKK | vehicle | VPgXFLKK_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgDFLAK | vehicle | VPgDFLAK_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_BOMBE | vehicle | VP_BOMBE_MTL.ILBM.png | - |
| VPfTTTTT | vehicle | VPfTTTTT_CITY1.ILBM.png, VPfTTTTT_FAERROBO.ILBM.png, VPfTTTTT_FX2.ILBM.png, VPfTTTTT_HUBI.ILBM.png | 21119701.ANM.png, 21119702.ANM.png, 21119703.ANM.png |
| VPgTTTTT | vehicle | VPgTTTTT_FX2.ILBM.png | GENES4-1.ANM.png |
| VP_TTTTT | vehicle | VP_TTTTT_CITY1.ILBM.png, VP_TTTTT_FAERROBO.ILBM.png, VP_TTTTT_HUBI.ILBM.png | - |
| VPgROBO | vehicle | VPgROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgKROBO | vehicle | VPgKROBO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPgBRGRO | vehicle | VPgBRGRO_FX2.ILBM.png | GENES4-1.ANM.png |
| VPgTAERO | vehicle | VPgTAERO_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_GIGAL | vehicle | VP_GIGAL_FX1.ILBM.png | - |
| VP_PHAN1 | vehicle | VP_PHAN1_FX1.ILBM.png, VP_PHAN1_HUBI.ILBM.png | 1212970A.ANM.png, 1212970B.ANM.png |
| OP_R4__1 | vehicle | OP_R4__1_FX1.ILBM.png | - |
| OP_R4__2 | vehicle | OP_R4__2_FX1.ILBM.png | - |
| OP_R4__3 | vehicle | OP_R4__3_FX1.ILBM.png | - |
| VPGBSECT | vehicle | VPGBSECT_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPGSULG1 | vehicle | VPGSULG1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_SULG2 | vehicle | VP_SULG2_FX1.ILBM.png | 12109601.ANM.png |
| VPGSULG5 | vehicle | VPGSULG5_FX2.ILBM.png | GENES3-1.ANM.png |
| VP_MYKOF | vehicle | VP_MYKOF_BODEN5.ILBM.png, VP_MYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VPfMYKOF | vehicle | VPfMYKOF_BODEN5.ILBM.png, VPfMYKOF_FX2.ILBM.png | 08019801.ANM.png, 08019802.ANM.png, 08019803.ANM.png, 08019804.ANM.png, 08019807.ANM.png, 08019808.ANM.png, 08019809.ANM.png, 0901970A.ANM.png |
| VP_HUBI5 | vehicle | VP_HUBI5_FX2.ILBM.png, VP_HUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png |
| VPwHUBI5 | vehicle | VPwHUBI5_HUBI.ILBM.png | - |
| VPfHUBI5 | vehicle | VPfHUBI5_FX2.ILBM.png, VPfHUBI5_HUBI.ILBM.png | 23019801.ANM.png, 23019802.ANM.png, 2301980A.ANM.png, HOTSHOT1.ANM.png |
| VPgHUBI5 | vehicle | VPgHUBI5_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VPxHUBI5 | vehicle | VPxHUBI5_HUBI.ILBM.png | - |
| VP_FLUG2 | vehicle | VP_FLUG2_FAERROBO.ILBM.png, VP_FLUG2_FHUBI.ILBM.png, VP_FLUG2_FX2.ILBM.png, VP_FLUG2_HUBI.ILBM.png | 27019800.ANM.png |
| VPxFLUG2 | vehicle | VPxFLUG2_FAERROBO.ILBM.png, VPxFLUG2_FHUBI.ILBM.png, VPxFLUG2_HUBI.ILBM.png | - |
| VPwFLUG2 | vehicle | VPwFLUG2_FAERROBO.ILBM.png, VPwFLUG2_FHUBI.ILBM.png, VPwFLUG2_HUBI.ILBM.png, VPwFLUG2_MTL.ILBM.png | - |
| VPgFLUG2 | vehicle | VPgFLUG2_FX2.ILBM.png | GENES4-1.ANM.png |
| VPfFLUG2 | vehicle | VPfFLUG2_FAERROBO.ILBM.png, VPfFLUG2_FHUBI.ILBM.png, VPfFLUG2_FX2.ILBM.png, VPfFLUG2_HUBI.ILBM.png | 27019800.ANM.png, 2701980A.ANM.png |
| VP_TRAIN | vehicle | VP_TRAIN_MTL.ILBM.png | - |
| VP_BLUU1 | vehicle | VP_BLUU1_FX1.ILBM.png | - |
| VP_SUPAB | vehicle | VP_SUPAB_FX1.ILBM.png | 250997XX.ANM.png |
| VP_FLBMB | vehicle | VP_FLBMB_FHUBI.ILBM.png, VP_FLBMB_HUBI.ILBM.png | 10039703.ANM.png |
| VPgTRAIN | vehicle | VPgTRAIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_TRAI1 | vehicle | VP_TRAI1_MTL.ILBM.png | - |
| VPgTRAI1 | vehicle | VPgTRAI1_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_ANI1 | vehicle | VP_ANI1_FX1.ILBM.png | - |
| VP_ANI2 | vehicle | VP_ANI2_FX1.ILBM.png | - |
| VP_ANI3 | vehicle | VP_ANI3_FX1.ILBM.png | - |
| VP_ANI4 | vehicle | VP_ANI4_FX2.ILBM.png | - |
| VP_WUCH1 | vehicle | VP_WUCH1_FX2.ILBM.png | - |
| VP_WUCH2 | vehicle | VP_WUCH2_FX2.ILBM.png | - |
| VP_WUCH3 | vehicle | VP_WUCH3_FX2.ILBM.png | - |
| VP_WUCH4 | vehicle | VP_WUCH4_FX2.ILBM.png | - |
| VP_WUCH5 | vehicle | VP_WUCH5_FX2.ILBM.png | - |
| VP_GRAN9 | vehicle | VP_GRAN9_FHUBI.ILBM.png, VP_GRAN9_HUBI.ILBM.png | 10039703.ANM.png |
| VP_NEU01 | vehicle | VP_NEU01_FX2.ILBM.png | - |
| VP_NEU02 | vehicle | VP_NEU02_FX2.ILBM.png | 22069801.ANM.png |
| VP_NEU03 | vehicle | VP_NEU03_FX1.ILBM.png | - |
| VP_NEU04 | vehicle | VP_NEU04_FX2.ILBM.png | - |
| VP_NEU05 | vehicle | VP_NEU05_FX2.ILBM.png | - |
| VP_NEU06 | vehicle | VP_NEU06_FX2.ILBM.png | - |
| VP_RAKT9 | vehicle | VP_RAKT9_FX2.ILBM.png, VP_RAKT9_HUBI.ILBM.png | 25069801.ANM.png |
| VP_GRANA | vehicle | VP_GRANA_FHUBI.ILBM.png, VP_GRANA_HUBI.ILBM.png | 10039703.ANM.png |
| VP_TKATJ | vehicle | VP_TKATJ_FAERROBO.ILBM.png, VP_TKATJ_HUBI.ILBM.png | 15109801.ANM.png |
| VPfTKATJ | vehicle | VPfTKATJ_FAERROBO.ILBM.png, VPfTKATJ_FX2.ILBM.png, VPfTKATJ_HUBI.ILBM.png | 15109801.ANM.png, 15109802.ANM.png, 15109803.ANM.png, HOTSHOT1.ANM.png |
| VPwTKATJ | vehicle | VPwTKATJ_FAERROBO.ILBM.png, VPwTKATJ_HUBI.ILBM.png | - |
| VPgTKATJ | vehicle | VPgTKATJ_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png, GENES6-1.ANM.png |
| VP_TODIN | vehicle | VP_TODIN_FAERROBO.ILBM.png, VP_TODIN_HUBI.ILBM.png | 20109801.ANM.png |
| VPfTODIN | vehicle | VPfTODIN_FAERROBO.ILBM.png, VPfTODIN_FX2.ILBM.png, VPfTODIN_HUBI.ILBM.png | 20109801.ANM.png, 20109802.ANM.png, 20109803.ANM.png |
| VPwTODIN | vehicle | VPwTODIN_FAERROBO.ILBM.png, VPwTODIN_HUBI.ILBM.png | - |
| VPgTODIN | vehicle | VPgTODIN_FX2.ILBM.png | GENES3-1.ANM.png, GENES4-1.ANM.png |
| VP_MMYKO | vehicle | VP_MMYKO_AIR1TXT.ILBM.png, VP_MMYKO_FX2.ILBM.png | 21109801.ANM.png, 21109802.ANM.png, 21109803.ANM.png, 21109804.ANM.png |
| VPwMMYKO | vehicle | VPwMMYKO_AIR1TXT.ILBM.png | - |
| VPgMMYKO | vehicle | VPgMMYKO_FX2.ILBM.png | GENES3-1.ANM.png |
| ST_EMPTY | building | ST_EMPTY_BODEN2.ILBM.png | - |
| GR_EMTPY | building | GR_EMTPY_BODEN1.ILBM.png | - |
| GS_EMPTY | building | GS_EMPTY_BODEN3.ILBM.png | - |
| ST_CITY1 | building | ST_CITY1_BERUD.ILBM.png, ST_CITY1_BODEN2.ILBM.png, ST_CITY1_CITY1.ILBM.png | - |
| STxCITY1 | building | STxCITY1_BODEN2.ILBM.png, STxCITY1_FBERUD.ILBM.png, STxCITY1_FCITY1.ILBM.png | - |
| STyCITY1 | building | STyCITY1_BODEN2.ILBM.png, STyCITY1_FBERUD.ILBM.png, STyCITY1_FCITY1.ILBM.png | - |
| STzCITYn | building | STzCITYn_BODEN2.ILBM.png | - |
| ST_CITY2 | building | ST_CITY2_BERUD.ILBM.png, ST_CITY2_BODEN2.ILBM.png, ST_CITY2_CITY1.ILBM.png | LEUCHT.png |
| STxCITY2 | building | STxCITY2_BODEN2.ILBM.png, STxCITY2_FBERUD.ILBM.png, STxCITY2_FCITY1.ILBM.png | - |
| STyCITY2 | building | STyCITY2_BODEN2.ILBM.png, STyCITY2_FBERUD.ILBM.png, STyCITY2_FCITY1.ILBM.png | - |
| ST_MUSE | building | ST_MUSE_BERUD.ILBM.png, ST_MUSE_BODEN2.ILBM.png, ST_MUSE_CITY1.ILBM.png | - |
| STxMUSE | building | STxMUSE_BODEN2.ILBM.png, STxMUSE_FBERUD.ILBM.png, STxMUSE_FCITY1.ILBM.png | - |
| STyMUSE | building | STyMUSE_BODEN2.ILBM.png, STyMUSE_FBERUD.ILBM.png, STyMUSE_FCITY1.ILBM.png | - |
| StzMUSE | building | StzMUSE_BODEN2.ILBM.png | - |
| ST_HO | building | ST_HO_BERUD.ILBM.png, ST_HO_BODEN2.ILBM.png, ST_HO_CITY1.ILBM.png | LICHT2.png, LICHT3.png |
| STxHO | building | STxHO_BODEN2.ILBM.png, STxHO_FBERUD.ILBM.png, STxHO_FCITY1.ILBM.png | - |
| STyHO | building | STyHO_BODEN2.ILBM.png, STyHO_FBERUD.ILBM.png, STyHO_FCITY1.ILBM.png | - |
| STzHO | building | STzHO_BODEN2.ILBM.png, STzHO_FBERUD.ILBM.png, STzHO_FCITY1.ILBM.png | - |
| ST_GHTT1 | building | ST_GHTT1_BERUD.ILBM.png, ST_GHTT1_BODEN2.ILBM.png | - |
| STxGHTT1 | building | STxGHTT1_BERUD.ILBM.png, STxGHTT1_BODEN2.ILBM.png, STxGHTT1_FBERUD.ILBM.png | - |
| STyGHTT1 | building | STyGHTT1_BERUD.ILBM.png, STyGHTT1_BODEN2.ILBM.png, STyGHTT1_FBERUD.ILBM.png | - |
| ST_STREA | building | ST_STREA_BODEN1.ILBM.png, ST_STREA_BODEN4.ILBM.png | - |
| ST_GHTT2 | building | ST_GHTT2_BERUD.ILBM.png, ST_GHTT2_BODEN2.ILBM.png | - |
| STxGHTT2 | building | STxGHTT2_BERUD.ILBM.png, STxGHTT2_BODEN2.ILBM.png, STxGHTT2_FBERUD.ILBM.png | - |
| STyGHTT2 | building | STyGHTT2_BERUD.ILBM.png, STyGHTT2_BODEN2.ILBM.png, STyGHTT2_FBERUD.ILBM.png | - |
| ST_STREB | building | ST_STREB_BODEN1.ILBM.png, ST_STREB_BODEN4.ILBM.png | - |
| ST_GHTT3 | building | ST_GHTT3_BERUD.ILBM.png, ST_GHTT3_BODEN2.ILBM.png | - |
| STxGHTT3 | building | STxGHTT3_BERUD.ILBM.png, STxGHTT3_BODEN2.ILBM.png, STxGHTT3_FBERUD.ILBM.png | - |
| STyGHTT3 | building | STyGHTT3_BERUD.ILBM.png, STyGHTT3_BODEN2.ILBM.png, STyGHTT3_FBERUD.ILBM.png | - |
| ST_STRE8 | building | ST_STRE8_BODEN1.ILBM.png, ST_STRE8_BODEN4.ILBM.png | - |
| ST_GHTT4 | building | ST_GHTT4_BERUD.ILBM.png, ST_GHTT4_BODEN2.ILBM.png, ST_GHTT4_CITY1.ILBM.png | INSANE.ANM.png |
| STxGHTT4 | building | STxGHTT4_BERUD.ILBM.png, STxGHTT4_BODEN2.ILBM.png, STxGHTT4_CITY1.ILBM.png, STxGHTT4_FBERUD.ILBM.png | - |
| STyGHTT4 | building | STyGHTT4_BERUD.ILBM.png, STyGHTT4_BODEN2.ILBM.png, STyGHTT4_CITY1.ILBM.png, STyGHTT4_FBERUD.ILBM.png | - |
| ST_STRE9 | building | ST_STRE9_BODEN1.ILBM.png, ST_STRE9_BODEN4.ILBM.png | - |
| ST_KRATR | building | ST_KRATR_BODEN2.ILBM.png | - |
| ST_KRAT2 | building | ST_KRAT2_BODEN2.ILBM.png | - |
| GRxFLAK1 | building | GRxFLAK1_BODEN1.ILBM.png, GRxFLAK1_MACHT.ILBM.png | - |
| GR_FLECK | building | GR_FLECK_BODEN2.ILBM.png | - |
| GR_KRAT1 | building | GR_KRAT1_BODEN2.ILBM.png | - |
| ST_GAT2 | building | ST_GAT2_BODEN2.ILBM.png, ST_GAT2_MTL.ILBM.png | - |
| ST_GAT2O | building | ST_GAT2O_BODEN2.ILBM.png, ST_GAT2O_FX2.ILBM.png, ST_GAT2O_MTL.ILBM.png | 08079601.ANM.png |
| BPXMYKOE | building | BPXMYKOE_BODEN5.ILBM.png | - |
| ST_FLAK2 | building | ST_FLAK2_BODEN2.ILBM.png, ST_FLAK2_MTL.ILBM.png | - |
| STzFLAK2 | building | STzFLAK2_BODEN2.ILBM.png, STzFLAK2_MTL.ILBM.png | - |
| BP_KRADA | building | BP_KRADA_BODEN2.ILBM.png, BP_KRADA_FHUBI.ILBM.png, BP_KRADA_FHYPE.ILBM.png | - |
| BP_TRADA | building | BP_TRADA_BODEN2.ILBM.png, BP_TRADA_FHUBI.ILBM.png, BP_TRADA_TAERROBO.ILBM.png | - |
| ST_SLUM1 | building | ST_SLUM1_BERUD.ILBM.png, ST_SLUM1_BODEN2.ILBM.png | - |
| STxSLUM1 | building | STxSLUM1_BODEN2.ILBM.png, STxSLUM1_FBERUD.ILBM.png | - |
| StySLUM1 | building | StySLUM1_BODEN2.ILBM.png, StySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM1 | building | GR_SLUM1_BERUD.ILBM.png, GR_SLUM1_BODEN1.ILBM.png | - |
| GRxSLUM1 | building | GRxSLUM1_BODEN1.ILBM.png, GRxSLUM1_FBERUD.ILBM.png | - |
| GRySLUM1 | building | GRySLUM1_BODEN1.ILBM.png, GRySLUM1_FBERUD.ILBM.png | - |
| GR_SLUM3 | building | GR_SLUM3_BODEN1.ILBM.png, GR_SLUM3_SHRTTWND.ILBM.png | - |
| GRxSLUM3 | building | GRxSLUM3_BODEN1.ILBM.png, GRxSLUM3_FHRTTWND.ILBM.png | - |
| GRySLUM3 | building | GRySLUM3_BODEN1.ILBM.png, GRySLUM3_FHRTTWND.ILBM.png | - |
| GRzSLUM3 | building | GRzSLUM3_BODEN2.ILBM.png | - |
| GR_SLUM2 | building | GR_SLUM2_BERUD.ILBM.png, GR_SLUM2_BODEN1.ILBM.png | - |
| GRxSLUM2 | building | GRxSLUM2_BODEN1.ILBM.png, GRxSLUM2_FBERUD.ILBM.png | - |
| GRySLUM2 | building | GRySLUM2_BODEN1.ILBM.png, GRySLUM2_BODEN2.ILBM.png, GRySLUM2_FBERUD.ILBM.png | - |
| GRzSLUM2 | building | GRzSLUM2_BODEN1.ILBM.png, GRzSLUM2_BODEN2.ILBM.png | - |
| GS_BIG | building | GS_BIG_BODEN3.ILBM.png | - |
| GR_GITTR | building | GR_GITTR_BODEN2.ILBM.png, GR_GITTR_MACHT.ILBM.png, GR_GITTR_SHRTTWND.ILBM.png | - |
| GRxGITTR | building | GRxGITTR_BODEN2.ILBM.png, GRxGITTR_FHRTTWND.ILBM.png, GRxGITTR_MACHT.ILBM.png, GRxGITTR_SHRTTWND.ILBM.png | - |
| GRyGITTR | building | GRyGITTR_BODEN2.ILBM.png, GRyGITTR_MACHT.ILBM.png | - |
| GR_BOHR | building | GR_BOHR_BODEN1.ILBM.png, GR_BOHR_MACHT.ILBM.png | - |
| GRXBOHR | building | GRXBOHR_BODEN1.ILBM.png, GRXBOHR_MACHT.ILBM.png | - |
| GRYBOHR | building | GRYBOHR_BODEN1.ILBM.png, GRYBOHR_MACHT.ILBM.png | - |
| ST_HO2 | building | ST_HO2_BODEN2.ILBM.png, ST_HO2_FMACHT.ILBM.png | - |
| STxHO2 | building | STxHO2_BODEN2.ILBM.png, STxHO2_FMACHT.ILBM.png | - |
| STyHO2 | building | STyHO2_BODEN2.ILBM.png, STyHO2_FMACHT.ILBM.png | - |
| STzHO2 | building | STzHO2_BODEN2.ILBM.png | - |
| ST_STRE1 | building | ST_STRE1_BODEN1.ILBM.png | - |
| ST_STRE3 | building | ST_STRE3_BODEN2.ILBM.png, ST_STRE3_BODEN4.ILBM.png | - |
| ST_STRE4 | building | ST_STRE4_BODEN2.ILBM.png | - |
| ST_STRE5 | building | ST_STRE5_BODEN2.ILBM.png | - |
| ST_SLUM2 | building | ST_SLUM2_BERUD.ILBM.png, ST_SLUM2_BODEN2.ILBM.png, ST_SLUM2_FBERUD.ILBM.png, ST_SLUM2_SHRTTWND.ILBM.png | - |
| STxSLUM2 | building | STxSLUM2_BODEN2.ILBM.png, STxSLUM2_FBERUD.ILBM.png, STxSLUM2_FHRTTWND.ILBM.png | - |
| STySLUM2 | building | STySLUM2_BODEN1.ILBM.png, STySLUM2_BODEN2.ILBM.png, STySLUM2_FBERUD.ILBM.png, STySLUM2_FHRTTWND.ILBM.png | - |
| GR_ETAG | building | GR_ETAG_BODEN1.ILBM.png, GR_ETAG_MACHT.ILBM.png | - |
| GRxETAG | building | GRxETAG_BODEN1.ILBM.png, GRxETAG_MACHT.ILBM.png | - |
| GRyETAG | building | GRyETAG_BODEN1.ILBM.png, GRyETAG_MACHT.ILBM.png | - |
| ST_HAUSL | building | ST_HAUSL_BODEN2.ILBM.png, ST_HAUSL_SCHROTT.ILBM.png | - |
| STXHAUSL | building | STXHAUSL_BODEN2.ILBM.png, STXHAUSL_FSCHROTT.ILBM.png | - |
| STYHAUSL | building | STYHAUSL_BODEN2.ILBM.png, STYHAUSL_FSCHROTT.ILBM.png | - |
| STzHAUSL | building | STzHAUSL_BODEN2.ILBM.png | - |
| ST_KUEHL | building | ST_KUEHL_BODEN2.ILBM.png, ST_KUEHL_SCHROTT.ILBM.png | - |
| STXKUEHL | building | STXKUEHL_BODEN2.ILBM.png, STXKUEHL_FSCHROTT.ILBM.png | - |
| STYKUEHL | building | STYKUEHL_BODEN2.ILBM.png, STYKUEHL_FSCHROTT.ILBM.png | - |
| GR_FABR1 | building | GR_FABR1_BODEN1.ILBM.png, GR_FABR1_SCHROTT.ILBM.png | - |
| GRxFABR1 | building | GRxFABR1_BODEN1.ILBM.png, GRxFABR1_FSCHROTT.ILBM.png | - |
| GRyFABR1 | building | GRyFABR1_BODEN1.ILBM.png, GRyFABR1_FSCHROTT.ILBM.png | - |
| GRzFABR1 | building | GRzFABR1_BODEN1.ILBM.png, GRzFABR1_BODEN4.ILBM.png | - |
| GR_FABR2 | building | GR_FABR2_SCHROTT.ILBM.png, GR_FABR2_SHRTTWND.ILBM.png | - |
| GRxFABR2 | building | GRxFABR2_FHRTTWND.ILBM.png, GRxFABR2_FSCHROTT.ILBM.png | - |
| GRyFABR2 | building | GRyFABR2_FHRTTWND.ILBM.png, GRyFABR2_FSCHROTT.ILBM.png | - |
| GRzFABR2 | building | GRzFABR2_BODEN4.ILBM.png | - |
| GR_LAGER | building | GR_LAGER_BODEN1.ILBM.png, GR_LAGER_SCHROTT.ILBM.png, GR_LAGER_TAERROBO.ILBM.png | - |
| GRxLAGER | building | GRxLAGER_BODEN1.ILBM.png, GRxLAGER_FSCHROTT.ILBM.png, GRxLAGER_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| ST_RUND | building | ST_RUND_BERUD.ILBM.png, ST_RUND_BODEN2.ILBM.png, ST_RUND_SCHROTT.ILBM.png | - |
| STxRUND | building | STxRUND_BODEN2.ILBM.png, STxRUND_FBERUD.ILBM.png, STxRUND_FSCHROTT.ILBM.png | - |
| STyRUND | building | STyRUND_BODEN2.ILBM.png, STyRUND_FBERUD.ILBM.png, STyRUND_FSCHROTT.ILBM.png | - |
| STzRUND | building | STzRUND_BODEN2.ILBM.png | - |
| GR_TVTRM | building | GR_TVTRM_BODEN2.ILBM.png, GR_TVTRM_CITY1.ILBM.png, GR_TVTRM_SCHROTT.ILBM.png | LEUCHTWARNER.png |
| GRXTVTRM | building | GRXTVTRM_BODEN2.ILBM.png, GRXTVTRM_FBERUD.ILBM.png, GRXTVTRM_FCITY1.ILBM.png, GRXTVTRM_FSCHROTT.ILBM.png | - |
| GRYTVTRM | building | GRYTVTRM_BODEN2.ILBM.png, GRYTVTRM_FSCHROTT.ILBM.png | - |
| GRZTVTRM | building | GRZTVTRM_BODEN2.ILBM.png | - |
| ST_CITY3 | building | ST_CITY3_BODEN2.ILBM.png, ST_CITY3_HYPE.ILBM.png, ST_CITY3_SHRTTWND.ILBM.png | - |
| STXCITY3 | building | STXCITY3_BODEN2.ILBM.png, STXCITY3_FHRTTWND.ILBM.png, STXCITY3_FHYPE.ILBM.png | - |
| STYCITY3 | building | STYCITY3_BODEN2.ILBM.png, STYCITY3_FBERUD.ILBM.png, STYCITY3_FHRTTWND.ILBM.png, STYCITY3_FHYPE.ILBM.png | - |
| STZCITY3 | building | STZCITY3_BODEN2.ILBM.png | - |
| GR_TEMP2 | building | GR_TEMP2_BODEN1.ILBM.png, GR_TEMP2_MACHT.ILBM.png | - |
| GRxTEMP2 | building | GRxTEMP2_BODEN1.ILBM.png, GRxTEMP2_FMACHT.ILBM.png, GRxTEMP2_MACHT.ILBM.png | - |
| GRyTEMP2 | building | GRyTEMP2_BODEN1.ILBM.png, GRyTEMP2_FMACHT.ILBM.png, GRyTEMP2_MACHT.ILBM.png | - |
| GRzTEMP2 | building | GRzTEMP2_BODEN1.ILBM.png | - |
| ST_ENDL1 | building | ST_ENDL1_BODEN5.ILBM.png, ST_ENDL1_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL2 | building | ST_ENDL2_BODEN5.ILBM.png, ST_ENDL2_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL3 | building | ST_ENDL3_BODEN5.ILBM.png, ST_ENDL3_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL4 | building | ST_ENDL4_BODEN5.ILBM.png, ST_ENDL4_FX2.ILBM.png | 10129701.ANM.png, 10129702.ANM.png, 10129703.ANM.png, 10129704.ANM.png, 10129705.ANM.png, 10129706.ANM.png |
| ST_ENDL5 | building | ST_ENDL5_BODEN5.ILBM.png, ST_ENDL5_FX2.ILBM.png, ST_ENDL5_MTL.ILBM.png | 0312970A.ANM.png, 0312970B.ANM.png, 0312970C.ANM.png, 0312970D.ANM.png, 0312970E.ANM.png, 0312970F.ANM.png, 0312970G.ANM.png, 14099701.ANM.png, 14099702.ANM.png |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| BP_SUPRA | building | BP_SUPRA_BODEN1.ILBM.png, BP_SUPRA_BODEN3.ILBM.png, BP_SUPRA_FAERROBO.ILBM.png, BP_SUPRA_TAERROBO.ILBM.png | - |
| ST_HYPE | building | ST_HYPE_BODEN2.ILBM.png, ST_HYPE_HYPE.ILBM.png, ST_HYPE_MACHT.ILBM.png, ST_HYPE_SHRTTWND.ILBM.png | - |
| STxHYPE | building | STxHYPE_BODEN2.ILBM.png, STxHYPE_FHRTTWND.ILBM.png, STxHYPE_FHYPE.ILBM.png, STxHYPE_MACHT.ILBM.png | - |
| STyHYPE | building | STyHYPE_BODEN2.ILBM.png, STyHYPE_FHRTTWND.ILBM.png, STyHYPE_FHYPE.ILBM.png, STyHYPE_MACHT.ILBM.png | - |
| STzHYPE | building | STzHYPE_BODEN2.ILBM.png, STzHYPE_FSCHROTT.ILBM.png | - |
| ST_BLOX1 | building | ST_BLOX1_BODEN2.ILBM.png, ST_BLOX1_FSCHROTT.ILBM.png | - |
| ST_BLOX2 | building | ST_BLOX2_BODEN2.ILBM.png, ST_BLOX2_FSCHROTT.ILBM.png | - |
| STXKFLAA | building | STXKFLAA_BODEN2.ILBM.png, STXKFLAA_FHYPE.ILBM.png | - |
| STZKFLAA | building | STZKFLAA_BODEN2.ILBM.png, STZKFLAA_FHYPE.ILBM.png | - |
| ST_KFLAA | building | ST_KFLAA_BODEN2.ILBM.png, ST_KFLAA_FHYPE.ILBM.png | - |
| ST_KFLAB | building | ST_KFLAB_BODEN2.ILBM.png, ST_KFLAB_FHYPE.ILBM.png | - |
| GR_TEMPL | building | GR_TEMPL_BODEN1.ILBM.png, GR_TEMPL_MACHT.ILBM.png | - |
| GRxTEMPL | building | GRxTEMPL_BODEN1.ILBM.png, GRxTEMPL_FMACHT.ILBM.png, GRxTEMPL_MACHT.ILBM.png | - |
| GRyTEMPL | building | GRyTEMPL_BODEN1.ILBM.png, GRyTEMPL_FMACHT.ILBM.png, GRyTEMPL_MACHT.ILBM.png | - |
| GR_FLAK1 | building | GR_FLAK1_BODEN1.ILBM.png, GR_FLAK1_MACHT.ILBM.png | - |
| ST_MACHT | building | ST_MACHT_BODEN2.ILBM.png, ST_MACHT_MACHT.ILBM.png, ST_MACHT_SCHROTT.ILBM.png | - |
| STxMACHT | building | STxMACHT_BODEN2.ILBM.png, STxMACHT_FMACHT.ILBM.png, STxMACHT_FSCHROTT.ILBM.png | - |
| STyMACHT | building | STyMACHT_BODEN2.ILBM.png, STyMACHT_FMACHT.ILBM.png, STyMACHT_FSCHROTT.ILBM.png | - |
| BP_POWR1 | building | BP_POWR1_BODEN2.ILBM.png, BP_POWR1_HYPE.ILBM.png | - |
| BPxPOWR1 | building | BPxPOWR1_BODEN2.ILBM.png, BPxPOWR1_FHYPE.ILBM.png | - |
| BPyPOWR1 | building | BPyPOWR1_BODEN2.ILBM.png, BPyPOWR1_FHYPE.ILBM.png | - |
| ST_TFLA1 | building | ST_TFLA1_BODEN2.ILBM.png, ST_TFLA1_TAERROBO.ILBM.png | - |
| STxTFLA1 | building | STxTFLA1_BODEN2.ILBM.png, STxTFLA1_FAERROBO.ILBM.png | - |
| STyTFLA1 | building | STyTFLA1_BODEN2.ILBM.png, STyTFLA1_FAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| GR_E_A1 | building | GR_E_A1_BODEN1.ILBM.png | - |
| GR_E_A2 | building | GR_E_A2_BODEN1.ILBM.png | - |
| GR_E_A3 | building | GR_E_A3_BODEN2.ILBM.png | - |
| GR_E_A4 | building | GR_E_A4_BODEN1.ILBM.png | - |
| ST_E_B1 | building | ST_E_B1_BODEN2.ILBM.png | - |
| ST_E_B2 | building | ST_E_B2_BODEN2.ILBM.png | - |
| ST_E_B3 | building | ST_E_B3_BODEN2.ILBM.png | - |
| ST_E_C1 | building | ST_E_C1_BODEN2.ILBM.png | - |
| ST_E_C2 | building | ST_E_C2_BODEN2.ILBM.png | - |
| GR_E_D1 | building | GR_E_D1_BODEN1.ILBM.png | - |
| GR_E_D2 | building | GR_E_D2_BODEN1.ILBM.png | - |
| GR_TV1 | building | GR_TV1_BERUD.ILBM.png, GR_TV1_BODEN1.ILBM.png, GR_TV1_MACHT.ILBM.png | - |
| GRxTV1 | building | GRxTV1_BERUD.ILBM.png, GRxTV1_BODEN1.ILBM.png, GRxTV1_FBERUD.ILBM.png, GRxTV1_FMACHT.ILBM.png | - |
| GRyTV1 | building | GRyTV1_BODEN1.ILBM.png, GRyTV1_FBERUD.ILBM.png, GRyTV1_FMACHT.ILBM.png | - |
| GRzTV1 | building | GRzTV1_BODEN1.ILBM.png, GRzTV1_BODEN4.ILBM.png | - |
| GR_TV2 | building | GR_TV2_BERUD.ILBM.png, GR_TV2_BODEN1.ILBM.png, GR_TV2_MACHT.ILBM.png | - |
| GRxTV2 | building | GRxTV2_BERUD.ILBM.png, GRxTV2_BODEN1.ILBM.png, GRxTV2_FBERUD.ILBM.png, GRxTV2_FMACHT.ILBM.png, GRxTV2_MACHT.ILBM.png | - |
| GRyTV2 | building | GRyTV2_BODEN1.ILBM.png, GRyTV2_FBERUD.ILBM.png, GRyTV2_FMACHT.ILBM.png | - |
| GRzTV2 | building | GRzTV2_BODEN1.ILBM.png, GRzTV2_BODEN4.ILBM.png | - |
| GR_TV3 | building | GR_TV3_BODEN1.ILBM.png, GR_TV3_CITY1.ILBM.png, GR_TV3_MACHT.ILBM.png | YPPSBPPS.ANM.png |
| GRxTV3 | building | GRxTV3_BODEN1.ILBM.png, GRxTV3_FCITY1.ILBM.png, GRxTV3_FMACHT.ILBM.png | - |
| GRyTV3 | building | GRyTV3_BODEN1.ILBM.png, GRyTV3_FCITY1.ILBM.png, GRyTV3_FMACHT.ILBM.png | - |
| GRzTV3 | building | GRzTV3_BODEN1.ILBM.png, GRzTV3_BODEN4.ILBM.png | - |
| BP_MRADA | building | BP_MRADA_BAGGER.ILBM.png, BP_MRADA_BODEN5.ILBM.png, BP_MRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049803.ANM.png, 29049806.ANM.png, 29049807.ANM.png, 29049808.ANM.png, 29049809.ANM.png, 2904980A.ANM.png, 2904980B.ANM.png, 2904980C.ANM.png, 2904980D.ANM.png |
| BPxMRADA | building | BPxMRADA_BAGGER.ILBM.png, BPxMRADA_BODEN5.ILBM.png, BPxMRADA_FX2.ILBM.png | 29049801.ANM.png, 29049802.ANM.png, 29049807.ANM.png, 29049809.ANM.png |
| BPyMRADA | building | BPyMRADA_BAGGER.ILBM.png, BPyMRADA_BODEN5.ILBM.png | 29049801.ANM.png |
| BP_MLEEE | building | BP_MLEEE_BODEN5.ILBM.png | - |
| ST_HAUS1 | building | ST_HAUS1_BODEN2.ILBM.png, ST_HAUS1_BODEN4.ILBM.png, ST_HAUS1_SCHROTT.ILBM.png | - |
| STXHAUS1 | building | STXHAUS1_BODEN2.ILBM.png, STXHAUS1_BODEN4.ILBM.png, STXHAUS1_FSCHROTT.ILBM.png | - |
| STYHAUS1 | building | STYHAUS1_BODEN2.ILBM.png, STYHAUS1_BODEN4.ILBM.png, STYHAUS1_FSCHROTT.ILBM.png | - |
| STzHAUS1 | building | STzHAUS1_BODEN2.ILBM.png, STzHAUS1_BODEN4.ILBM.png | - |
| ST_HAUS2 | building | ST_HAUS2_BODEN2.ILBM.png, ST_HAUS2_BODEN4.ILBM.png, ST_HAUS2_SCHROTT.ILBM.png | - |
| STxHAUS2 | building | STxHAUS2_BODEN2.ILBM.png, STxHAUS2_BODEN4.ILBM.png, STxHAUS2_FSCHROTT.ILBM.png | - |
| STyHAUS2 | building | STyHAUS2_BODEN2.ILBM.png, STyHAUS2_BODEN4.ILBM.png, STyHAUS2_FSCHROTT.ILBM.png | - |
| STzHAUS2 | building | STzHAUS2_BODEN2.ILBM.png, STzHAUS2_BODEN4.ILBM.png | - |
| ST_STRWS | building | ST_STRWS_BODEN1.ILBM.png | - |
| ST_STRE7 | building | ST_STRE7_BODEN1.ILBM.png, ST_STRE7_FHUBI.ILBM.png | - |
| STxSTRE7 | building | STxSTRE7_BODEN1.ILBM.png, STxSTRE7_FHUBI.ILBM.png | - |
| STxENDL1 | building | STxENDL1_BODEN5.ILBM.png | - |
| STxENDL2 | building | STxENDL2_BODEN5.ILBM.png | - |
| STxENDL3 | building | STxENDL3_BODEN5.ILBM.png | - |
| STxENDL4 | building | STxENDL4_BODEN5.ILBM.png | - |
| STxENDL5 | building | STxENDL5_BODEN5.ILBM.png, STxENDL5_MTL.ILBM.png | 14099701.ANM.png |
| ST_MLEER | building | ST_MLEER_BODEN5.ILBM.png | - |
| BP_MMMMM | building | BP_MMMMM_BODEN5.ILBM.png | - |
| BP_SUPA1 | building | BP_SUPA1_MTL.ILBM.png, BP_SUPA1_TAERROBO.ILBM.png | - |
| BP_SUPA2 | building | BP_SUPA2_FX2.ILBM.png, BP_SUPA2_MTL.ILBM.png, BP_SUPA2_TAERROBO.ILBM.png | 11029801.ANM.png, 11029802.ANM.png, 11029803.ANM.png, 11029804.ANM.png |
| BP_SUPA3 | building | BP_SUPA3_MTL.ILBM.png | - |
| BP_SIKEY | building | BP_SIKEY_BODEN2.ILBM.png, BP_SIKEY_MTL.ILBM.png, BP_SIKEY_TAERROBO.ILBM.png | - |
| dummy | building | (empty model) | |
| dummy | building | (empty model) | |
| MT_EMPTY | building | MT_EMPTY_MTL.ILBM.png | - |
| MT_EASY2 | building | MT_EASY2_MTL.ILBM.png | - |
| MTxEASY2 | building | MTxEASY2_MTL.ILBM.png | - |
| MTyEASY2 | building | MTyEASY2_MTL.ILBM.png | - |
| MTzEASY2 | building | MTzEASY2_BODEN2.ILBM.png, MTzEASY2_MTL.ILBM.png | - |
| MT_POWR2 | building | MT_POWR2_BODEN2.ILBM.png, MT_POWR2_FX2.ILBM.png, MT_POWR2_MTL.ILBM.png | 19069607.ANM.png, 19069608.ANM.png, 1906960D.ANM.png, 1906960E.ANM.png, 1906960F.ANM.png, 1906960G.ANM.png, 1906960H.ANM.png, 1906960I.ANM.png, 1906960J.ANM.png |
| MTxPOWR2 | building | MTxPOWR2_BODEN2.ILBM.png, MTxPOWR2_FX2.ILBM.png, MTxPOWR2_MTL.ILBM.png | 1906960D.ANM.png, 1906960G.ANM.png, 1906960K.ANM.png, 1906960L.ANM.png, 1906960M.ANM.png |
| MTyPOWR2 | building | MTyPOWR2_BODEN2.ILBM.png, MTyPOWR2_MTL.ILBM.png | - |
| MTzPOWR2 | building | MTzPOWR2_BODEN2.ILBM.png, MTzPOWR2_MTL.ILBM.png | - |
| ST_GATE | building | ST_GATE_BODEN1.ILBM.png, ST_GATE_BODEN2.ILBM.png, ST_GATE_BODEN4.ILBM.png, ST_GATE_MTL.ILBM.png | - |
| ST_GATEO | building | ST_GATEO_BODEN1.ILBM.png, ST_GATEO_BODEN2.ILBM.png, ST_GATEO_BODEN4.ILBM.png, ST_GATEO_FX2.ILBM.png, ST_GATEO_MTL.ILBM.png | 08079601.ANM.png |
| GR_252 | building | GR_252_BODEN1.ILBM.png, GR_252_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_253 | building | GR_253_BODEN1.ILBM.png, GR_253_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_254 | building | GR_254_BODEN1.ILBM.png, GR_254_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_255 | building | GR_255_BODEN1.ILBM.png, GR_255_FX2.ILBM.png | 05079601.ANM.png, 05079602.ANM.png, 05079603.ANM.png |
| GR_248 | building | GR_248_BODEN1.ILBM.png | - |
| ST_GEM1 | building | ST_GEM1_BODEN2.ILBM.png, ST_GEM1_FHYPE.ILBM.png | - |
| STxGEM1 | building | STxGEM1_BODEN2.ILBM.png, STxGEM1_FHYPE.ILBM.png, STxGEM1_FMACHT.ILBM.png | - |
| STyGEM1 | building | STyGEM1_BODEN2.ILBM.png, STyGEM1_FHYPE.ILBM.png, STyGEM1_FMACHT.ILBM.png | - |
| STzGEM1 | building | STzGEM1_BODEN2.ILBM.png | - |
| ST_GEM2 | building | ST_GEM2_BODEN2.ILBM.png, ST_GEM2_FHYPE.ILBM.png | - |
| STxGEM2 | building | STxGEM2_BODEN2.ILBM.png, STxGEM2_FHYPE.ILBM.png, STxGEM2_FMACHT.ILBM.png | - |
| STyGEM2 | building | STyGEM2_BODEN2.ILBM.png, STyGEM2_FHYPE.ILBM.png, STyGEM2_FMACHT.ILBM.png | - |
| ST_GEMT | building | ST_GEMT_BODEN1.ILBM.png, ST_GEMT_BODEN4.ILBM.png, ST_GEMT_FHYPE.ILBM.png, ST_GEMT_FX1.ILBM.png | 17079601.ANM.png |
| STxGEMT | building | STxGEMT_BODEN1.ILBM.png, STxGEMT_BODEN4.ILBM.png, STxGEMT_FHYPE.ILBM.png | - |
| STzGEMT | building | STzGEMT_BODEN1.ILBM.png, STzGEMT_BODEN2.ILBM.png, STzGEMT_BODEN4.ILBM.png | - |
| ST_GEMM | building | ST_GEMM_BODEN2.ILBM.png, ST_GEMM_FHYPE.ILBM.png | - |
| STxGEMM | building | STxGEMM_BODEN2.ILBM.png, STxGEMM_FHYPE.ILBM.png | - |
| ST_GEMM2 | building | ST_GEMM2_BODEN2.ILBM.png, ST_GEMM2_FHYPE.ILBM.png | - |
| STxGEMM2 | building | STxGEMM2_BODEN2.ILBM.png, STxGEMM2_FHYPE.ILBM.png | - |
| BP_MYKOE | building | BP_MYKOE_BODEN5.ILBM.png, BP_MYKOE_FX2.ILBM.png | ARGBLTZ.ANM.png, BRGBLTZ.ANM.png, CRGBLTZ.ANM.png |
| ST_NS1 | building | ST_NS1_BODEN1.ILBM.png, ST_NS1_FHUBI.ILBM.png | - |
| ST_STRE2 | building | ST_STRE2_BODEN1.ILBM.png | - |
| ST_NS2 | building | ST_NS2_BODEN1.ILBM.png, ST_NS2_FHUBI.ILBM.png | - |
| ST_FLAK1 | building | ST_FLAK1_BODEN2.ILBM.png, ST_FLAK1_MTL.ILBM.png | - |
| STxFLAK1 | building | STxFLAK1_BODEN2.ILBM.png, STxFLAK1_MTL.ILBM.png | - |
| STyFLAK1 | building | STyFLAK1_BODEN2.ILBM.png, STyFLAK1_MTL.ILBM.png | - |
| STzFLAK1 | building | STzFLAK1_BODEN2.ILBM.png, STzFLAK1_MTL.ILBM.png | - |
| ST_RADAR | building | ST_RADAR_BODEN2.ILBM.png, ST_RADAR_FHUBI.ILBM.png, ST_RADAR_FX2.ILBM.png, ST_RADAR_MTL.ILBM.png | - |
| STxRADAR | building | STxRADAR_BODEN2.ILBM.png, STxRADAR_FHUBI.ILBM.png, STxRADAR_MTL.ILBM.png | - |
| BP_MFLAK | building | BP_MFLAK_BODEN5.ILBM.png | - |
| GS_STMF1 | building | GS_STMF1_BODEN3.ILBM.png, GS_STMF1_TAERROBO.ILBM.png | - |
| ST_KMPKT | building | ST_KMPKT_BODEN2.ILBM.png | - |
| ST_META1 | building | ST_META1_BODEN2.ILBM.png, ST_META1_FCITY1.ILBM.png, ST_META1_FMACHT.ILBM.png | - |
| STxMETA1 | building | STxMETA1_BODEN2.ILBM.png, STxMETA1_FCITY1.ILBM.png, STxMETA1_FMACHT.ILBM.png | - |
| STyMETA1 | building | STyMETA1_BODEN2.ILBM.png, STyMETA1_FCITY1.ILBM.png, STyMETA1_FMACHT.ILBM.png | - |
| ST_NSTR0 | building | ST_NSTR0_BODEN1.ILBM.png, ST_NSTR0_BODEN2.ILBM.png, ST_NSTR0_BODEN4.ILBM.png | - |
| ST_NSTR1 | building | ST_NSTR1_BODEN1.ILBM.png, ST_NSTR1_BODEN2.ILBM.png | - |
| ST_NSTR2 | building | ST_NSTR2_BODEN1.ILBM.png, ST_NSTR2_BODEN2.ILBM.png, ST_NSTR2_FHUBI.ILBM.png | - |
| STxNSTR2 | building | STxNSTR2_BODEN1.ILBM.png, STxNSTR2_BODEN2.ILBM.png, STxNSTR2_FHUBI.ILBM.png | - |
| STyNSTR2 | building | STyNSTR2_BODEN1.ILBM.png, STyNSTR2_BODEN2.ILBM.png | - |
| ST_NSTR3 | building | ST_NSTR3_BODEN1.ILBM.png, ST_NSTR3_BODEN2.ILBM.png, ST_NSTR3_BODEN4.ILBM.png | - |
| ST_NSTR4 | building | ST_NSTR4_BODEN1.ILBM.png, ST_NSTR4_BODEN4.ILBM.png | - |
| ST_NSTR5 | building | ST_NSTR5_BODEN1.ILBM.png, ST_NSTR5_BODEN2.ILBM.png, ST_NSTR5_BODEN4.ILBM.png | - |
| ST_NSTR6 | building | ST_NSTR6_BODEN1.ILBM.png, ST_NSTR6_BODEN2.ILBM.png, ST_NSTR6_BODEN4.ILBM.png | - |
| ST_NSTR7 | building | ST_NSTR7_BODEN2.ILBM.png, ST_NSTR7_BODEN4.ILBM.png | - |
| BPzMFLAK | building | BPzMFLAK_BODEN5.ILBM.png | - |
| S00H | slurp | S00H_BODEN1.ILBM.png | - |
| S01H | slurp | S01H_BODEN1.ILBM.png | - |
| S02H | slurp | S02H_BODEN3.ILBM.png | - |
| S03H | slurp | S03H_BODEN5.ILBM.png | - |
| S04H | slurp | S04H_BODEN1.ILBM.png | - |
| S05H | slurp | S05H_BODEN3.ILBM.png | - |
| S10H | slurp | S10H_BODEN1.ILBM.png | - |
| S11H | slurp | S11H_BODEN2.ILBM.png | - |
| S12H | slurp | S12H_BODEN3.ILBM.png | - |
| S13H | slurp | S13H_BODEN5.ILBM.png | - |
| S14H | slurp | S14H_BODEN2.ILBM.png | - |
| S15H | slurp | S15H_BODEN3.ILBM.png | - |
| S20H | slurp | S20H_BODEN3.ILBM.png | - |
| S21H | slurp | S21H_BODEN3.ILBM.png | - |
| S22H | slurp | S22H_BODEN3.ILBM.png | - |
| S23H | slurp | S23H_BODEN5.ILBM.png | - |
| S24H | slurp | S24H_BODEN3.ILBM.png | - |
| S25H | slurp | S25H_BODEN3.ILBM.png | - |
| S30H | slurp | S30H_BODEN5.ILBM.png | - |
| S31H | slurp | S31H_BODEN5.ILBM.png | - |
| S32H | slurp | S32H_BODEN5.ILBM.png | - |
| S33H | slurp | S33H_BODEN5.ILBM.png | - |
| S34H | slurp | S34H_BODEN5.ILBM.png | - |
| S35H | slurp | S35H_BODEN5.ILBM.png | - |
| S40H | slurp | S40H_BODEN1.ILBM.png | - |
| S41H | slurp | S41H_BODEN2.ILBM.png | - |
| S42H | slurp | S42H_BODEN3.ILBM.png | - |
| S43H | slurp | S43H_BODEN5.ILBM.png | - |
| S44H | slurp | S44H_BODEN1.ILBM.png, S44H_BODEN2.ILBM.png | - |
| S45H | slurp | S45H_BODEN3.ILBM.png | - |
| S50H | slurp | S50H_BODEN3.ILBM.png | - |
| S51H | slurp | S51H_BODEN3.ILBM.png | - |
| S52H | slurp | S52H_BODEN3.ILBM.png | - |
| S53H | slurp | S53H_BODEN5.ILBM.png | - |
| S54H | slurp | S54H_BODEN3.ILBM.png | - |
| S55H | slurp | S55H_BODEN3.ILBM.png, S55H_HYPE.ILBM.png | - |
| S00V | slurp | S00V_BODEN1.ILBM.png | - |
| S01V | slurp | S01V_BODEN1.ILBM.png | - |
| S02V | slurp | S02V_BODEN3.ILBM.png | - |
| S03V | slurp | S03V_BODEN5.ILBM.png | - |
| S04V | slurp | S04V_BODEN1.ILBM.png | - |
| S05V | slurp | S05V_BODEN3.ILBM.png | - |
| S10V | slurp | S10V_BODEN1.ILBM.png | - |
| S11V | slurp | S11V_BODEN2.ILBM.png | - |
| S12V | slurp | S12V_BODEN3.ILBM.png | - |
| S13V | slurp | S13V_BODEN5.ILBM.png | - |
| S14V | slurp | S14V_BODEN2.ILBM.png | - |
| S15V | slurp | S15V_BODEN3.ILBM.png | - |
| S20V | slurp | S20V_BODEN3.ILBM.png | - |
| S21V | slurp | S21V_BODEN3.ILBM.png | - |
| S22V | slurp | S22V_BODEN3.ILBM.png | - |
| S23V | slurp | S23V_BODEN5.ILBM.png | - |
| S24V | slurp | S24V_BODEN3.ILBM.png | - |
| S25V | slurp | S25V_BODEN3.ILBM.png | - |
| S30V | slurp | S30V_BODEN5.ILBM.png | - |
| S31V | slurp | S31V_BODEN5.ILBM.png | - |
| S32V | slurp | S32V_BODEN5.ILBM.png | - |
| S33V | slurp | S33V_BODEN5.ILBM.png | - |
| S34V | slurp | S34V_BODEN5.ILBM.png | - |
| S35V | slurp | S35V_BODEN5.ILBM.png | - |
| S40V | slurp | S40V_BODEN1.ILBM.png | - |
| S41V | slurp | S41V_BODEN2.ILBM.png | - |
| S42V | slurp | S42V_BODEN3.ILBM.png | - |
| S43V | slurp | S43V_BODEN5.ILBM.png | - |
| S44V | slurp | S44V_BODEN1.ILBM.png, S44V_BODEN2.ILBM.png | - |
| S45V | slurp | S45V_BODEN3.ILBM.png | - |
| S50V | slurp | S50V_BODEN3.ILBM.png | - |
| S51V | slurp | S51V_BODEN3.ILBM.png | - |
| S52V | slurp | S52V_BODEN3.ILBM.png | - |
| S53V | slurp | S53V_BODEN5.ILBM.png | - |
| S54V | slurp | S54V_BODEN3.ILBM.png | - |
| S55V | slurp | S55V_BODEN3.ILBM.png, S55V_HYPE.ILBM.png | - |
