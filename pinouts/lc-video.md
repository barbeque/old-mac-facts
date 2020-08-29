# LC video pinout

## All pins
|LC Pin  | Signal |
|--------|--------|
|1	| Red ground |
|2	| Red video |
|3, 15	| /CSYNC (Apple) or /HSYNC (VGA) depending on monitor used |
|4	| Monitor sense 0 |
|5	| Green video |
|6	| Green ground |
|7	| Monitor sense 1 (grounded internally on LC) |
|8	| N/C |
|9	| Blue video |
|10	| Monitor sense 2 |
|11	| Ground for c-sync and v-sync |
|12	| /VSYNC |
|13	| Blue ground |
|14	| /HSYNC ground |
|Shell	| Chassis ground |

| Sense combination | To Get .... |
|-------------------|-------------|
| SENSE0 grounded   | 640x480 |
| SENSE0 & SENSE2 grounded | 512x384 (12") |
| SENSE2 grounded   | VGA |

## VGA-relevant pins
| LC Pin | Signal                 |
|--------|------------------------|
|1	 | Red ground |
|2	 | Red video signal |
|5	 | Green video signal |
|6	 | Green ground |
|9	 | Blue video signal |
|13	 | Blue ground |
|15	 | /HSYNC |
|12	 | /VSYNC |
|14	 | HSYNC ground |
|7, 10	 | Tie SENSE1 & SENSE2 together for VGA output and timing |

## Sources:
 * [Soundpush](http://members.dodo.com.au/~soundpush/computers/projects/mac/mac_video.html)
