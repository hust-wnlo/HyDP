# HyDP
This is the design code file about HyDP.
# USAGE
### How to Configure?
The current version of HyDP supports built-in configuration
```c++
//Example in zns.c:1787
    spp->pg_rd_lat = NAND_READ_LATENCY;
    spp->pg_wr_lat = NAND_PROG_LATENCY;
    spp->blk_er_lat = NAND_ERASE_LATENCY;
    spp->ch_xfer_lat = NAND_CHNL_PAGE_TRANSFER_LATENCY;

    spp->nchnls         = 8;   //default : 8
    spp->chnls_per_zone = 1;   
    spp->zones          = n->num_zones;     
    spp->ways           = 2;    //default : 2
    spp->ways_per_zone  = 2;    //default :==spp->ways
    spp->dies_per_chip  = 1;    //default : 1
    spp->planes_per_die = 4;    //default : 4
    spp->register_model = 1;    
```
* to change configurations, 
  * SU-zone
  ```c++
      spp->chnls_per_zone = 1;   
      spp->ways_per_zone  = 1;    //default :==spp->ways
  ```
  * MU4-zone
  ```c++
      spp->chnls_per_zone = 4;    
      spp->ways_per_zone  = 1;    //default :==spp->ways
  ```
  * MU8-zone
  ```c++
      spp->chnls_per_zone = 8;    
      spp->ways_per_zone  = 1;    //default :==spp->ways
  ```
  * FU-zone(16)
  ```c++
      spp->chnls_per_zone = 8;    
      spp->ways_per_zone  = 2;    //default :==spp->ways

### Run FEMU as NVMe ZNS (Zoned-Namespace) SSDs (``ZNSSD`` mode)

**Notes:** Currently only basic ZNS interface is supported and it can be used
for development purposes.

```Bash
./run-zns.sh
```

### HyDP configurations

  NAND_READ_LATENCY    = 65000 65us TLC_tREAD(65us : 16K page time)
  NAND_PROG_LATENCY  = 450us TLC_tProg ,3D time
  NAND_ERASE_LATENCY = SLC_BLOCK_ERASE_LATENCY_NS,//2000000
  NAND_CHNL_PAGE_TRANSFER_LATENCY = 2.5? 1200MT = 9600MB/s = 390ns per 4K 
  //NAND_CHNL_PAGE_TRANSFER_LATENCY = 0,
  //SK Hynix read     : 400Mb/s for 1 chip..
  //WD ZN540 4TB read : avg 80us 
  //ZEMU read         : 
  //SK Hynix write    : 100Mb/s for 1 chip..
  //WD ZN540 4TB write: 
  //ZEMU write        : 5Mb/s for 1 chip...
