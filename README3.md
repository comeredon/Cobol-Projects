# z/OS example inventory

This inventory describes the sources retained in [Mainframe/ZOS](Mainframe/ZOS).
Source or JCL availability does not imply that an example has been tested on
your installation. See the [setup instructions and limitations](README.md).

## Normal batch examples

| Source | Description | Included JCL |
| :----- | :---------- | :----------- |
| [BDS0702](Mainframe/ZOS/Normal/cbl/BDS0702.cbl) | Read employee records | [BDS0702.jcl](Mainframe/ZOS/Normal/jcl/BDS0702.jcl) |
| [BDS0704](Mainframe/ZOS/Normal/cbl/BDS0704.cbl) | Read gadget records | [BDS0704.jcl](Mainframe/ZOS/Normal/jcl/BDS0704.jcl) |
| [BDS0801](Mainframe/ZOS/Normal/cbl/BDS0801.cbl) | Heading record | [BDS0801.jcl](Mainframe/ZOS/Normal/jcl/BDS0801.jcl) |
| [BDS0802](Mainframe/ZOS/Normal/cbl/BDS0802.cbl) | Footer record | [BDS0802.jcl](Mainframe/ZOS/Normal/jcl/BDS0802.jcl) |
| [BDS0803](Mainframe/ZOS/Normal/cbl/BDS0803.cbl) | Member report | [BDS0803.jcl](Mainframe/ZOS/Normal/jcl/BDS0803.jcl) |
| [BDS0804](Mainframe/ZOS/Normal/cbl/BDS0804.cbl) | Variable-length records | Not included |
| [BDS1001](Mainframe/ZOS/Normal/cbl/BDS1001.cbl) | Three-level control break | [BDS1001.jcl](Mainframe/ZOS/Normal/jcl/BDS1001.jcl) |
| [BDS1002](Mainframe/ZOS/Normal/cbl/BDS1002.cbl) | Two-level control break | [BDS1002.jcl](Mainframe/ZOS/Normal/jcl/BDS1002.jcl) |
| [BDS1003](Mainframe/ZOS/Normal/cbl/BDS1003.cbl) | File update | Not included |
| [BDS1004](Mainframe/ZOS/Normal/cbl/BDS1004.cbl) | Full file update | Not included |
| [CBL0106](Mainframe/ZOS/Normal/cbl/CBL0106.cbl) | Account report | [CBL0106J.jcl](Mainframe/ZOS/Normal/jcl/CBL0106J.jcl) |
| [EXE4](Mainframe/ZOS/Normal/cbl/EXE4.cbl) | Weather report | [EXE4.jcl](Mainframe/ZOS/Normal/jcl/EXE4.jcl) |
| [FAVRPT](Mainframe/ZOS/Normal/cbl/FAVRPT.cbl) | Favourites report | Not included |
| [ODS0001](Mainframe/ZOS/Normal/cbl/ODS0001.cbl) | Account-report tutorial variant | Not included |
| [ODS000C](Mainframe/ZOS/Normal/cbl/ODS000C.cbl) | Account record conversion | Not included |
| [ODS0106](Mainframe/ZOS/Normal/cbl/ODS0106.cbl) | Account-report tutorial variant | Not included |

The BDS examples follow
['Beginning COBOL for Programmers' by Michael Coughlan](http://www.apress.com/9781430262534).
The ODS examples follow
[the Open Mainframe Project COBOL training course](https://www.openmainframeproject.org/projects/coboltrainingcourse).

## Other retained z/OS examples

- [ECBAP sources](Mainframe/ZOS/ECBAP/cbl): reporting and validation workshops,
  table handling, and the MAINPGM/SUB01-SUB06 subprogram examples. The
  [course assignment history](README4.md) includes exercises whose source is
  not distributed here.
- [Internal-Sort](Mainframe/ZOS/Internal-Sort): five internal-sort examples,
  local copybooks, and [sample JCL](Mainframe/ZOS/Internal-Sort/jcl/sort.jcl.txt).
- [Zowe](Mainframe/ZOS/Zowe): initialization, data-set creation (including VSAM),
  and a simple report example. Review the existing setup limitations in the
  [main README](README.md) before using the scripts.

The [shared copybooks](common/cpy), [sample data](common/data), and
[IBM batch template](pgm_templates/Batch/slt_base_ibm_batch.cob) remain available.
