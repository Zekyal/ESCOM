//gcc -o LLC EnviaTramasLLC.c 
#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <string.h>

unsigned char MACorigen[6];
unsigned char IPorigen[4];
unsigned char MascaraSubred[4];
unsigned char trama_LLC_1[250]={0x00, 0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x2f ,0xf0 ,0xf0, 
0x03, 0x2c ,0x00 ,0xff ,0xef ,0x0e ,0x17 ,0x85 ,0x00 ,0x4f ,0x00 ,0x85 ,0x00 ,0x4d ,0x34 ,0x20, 
0x20, 0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x00 ,0x4d ,0x38 ,0x20, 
0x20, 0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20};
unsigned char trama_LLC_2[250]={0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x03 ,0xf0 ,0xf0, 
0x7f ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20};
unsigned char trama_LLC_3[250]={0x00 ,0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x03 ,0xf0 ,0xf1, 
0x73 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 }; 
unsigned char trama_LLC_4[250]={0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x04 ,0xf0 ,0xf0, 
0x01 ,0x01 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20};	 
unsigned char trama_LLC_5[250]={0x00 ,0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x04 ,0xf0 ,0xf1, 
0x01 ,0x01 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 };
unsigned char trama_LLC_6[250]={0x00 ,0x20 ,0x18 ,0x66 ,0xc6 ,0x02 ,0x00 ,0x00 ,0xe8 ,0x15 ,0xbb ,0x75 ,0x00 ,0x12 ,0xf0 ,0xf0, 
0x00 ,0x01 ,0x0e ,0x00 ,0xff ,0xef ,0x19 ,0x8f ,0xbc ,0x05 ,0x85 ,0x00 ,0x4f ,0x00 ,0x85 ,0x4f, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20 ,0x20};
unsigned char trama_LLC_7[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02 ,0x00 ,0x12 ,0xf0 ,0xf0, 
0x00, 0x03, 0x0e, 0x00, 0xff, 0xef, 0x17, 0x81, 0xbc, 0x05, 0x4f, 0x00 ,0x85 ,0x00 ,0x4f ,0x85, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20 ,0x20 ,0x20 ,0x20 ,0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_8[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x03, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_9[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x05, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_10[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x03, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_11[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x5f, 0xf0, 0xf0, 
0x02, 0x04, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x4f, 0x85, 
0xff, 0x53, 0x4d, 0x42, 0x72, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc1, 0x1d, 0x00, 0x00, 0x04, 0x2d, 
0x11, 0x05, 0x00, 0x02, 0x02, 0x00, 0x01, 0x00, 0x68, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 
0x85, 0x00, 0x01, 0x80, 0x03, 0x02, 0x00, 0x00, 0x00, 0x63, 0xbe, 0x4f, 0x3d, 0x66, 0xc1, 0x01, 
0x68, 0x01, 0x08, 0x08, 0x00, 0x85, 0x00, 0x01, 0x80, 0x9f, 0xfe, 0xe6, 0x3b};
unsigned char trama_LLC_12[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x04, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_13[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x05, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_14[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x05, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_15[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x86, 0xf0, 0xf0, 
0x04, 0x04, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x85, 0x4f, 
0xff, 0x53, 0x4d, 0x42, 0x73, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc1, 0x1d, 0x00, 0x00, 0x04, 0x2d, 
0x0d, 0x75, 0x00, 0x59, 0x00, 0x68, 0x0b, 0x02, 0x00, 0x00, 0x00, 0x85, 0x00, 0x01, 0x80, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00, 0x58, 
0x00, 0x57, 0x69, 0x6e, 0x64, 0x6f, 0x77, 0x73, 0x20, 0x34, 0x2e, 0x30, 0x00, 0x57, 0x69, 0x6e, 
0x64, 0x6f, 0x77, 0x73, 0x20, 0x34, 0x2e, 0x30, 0x00, 0x04, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x02, 0x00, 0x10, 0x00, 0x20, 0x00, 0x5c, 0x5c, 0x4d, 0x38, 0x5c, 0x49, 0x50, 0x43, 0x24, 0x00, 
0x49, 0x50, 0x43, 0x00};
unsigned char trama_LLC_16[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x46, 0xf0, 0xf0,
0x04, 0x06, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x4f, 0x85,
0xff, 0x53, 0x4d, 0x42, 0x73, 0x00, 0x00, 0x00, 0x00, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0xc1, 0x1d, 0x00, 0x00, 0x04, 0x2d, 
0x03, 0x75, 0x00, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x00, 0x00, 0x00, 0x04, 0x00, 
0x49, 0x50, 0x43, 0x00};
unsigned char trama_LLC_17[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x07, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_18[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1,
0x01, 0x07, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_19[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x78, 0xf0, 0xf0,
0x06, 0x06, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x85, 0x4f,
0xff, 0x53, 0x4d, 0x42, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0xc1, 0x1d, 0x00, 0x00, 0x04, 0x2e, 
0x0e, 0x1a, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x88, 0x13, 0x00, 
0x00, 0x00, 0x00, 0x1a, 0x00, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x27, 0x00, 0x5c, 
0x50, 0x49, 0x50, 0x45, 0x5c, 0x4c, 0x41, 0x4e, 0x4d, 0x41, 0x4e, 0x00, 0x68, 0x00, 0x57, 0x72, 
0x4c, 0x65, 0x68, 0x44, 0x4f, 0x00, 0x42, 0x31, 0x36, 0x42, 0x42, 0x44, 0x7a, 0x00, 0x01, 0x00, 
0x00, 0x10, 0x02, 0x22, 0x00, 0x00};
unsigned char trama_LLC_20[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x08, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_21[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x09, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_22[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x07, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_23[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0xbe, 0xf0, 0xf0, 
0x06, 0x08, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x4f, 0x85, 
0xff, 0x53, 0x4d, 0x42, 0x25, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0xc1, 0x1d, 0x00, 0x00, 0x04, 0x2e, 
0x0a, 0x08, 0x00, 0x6c, 0x00, 0x00, 0x00, 0x08, 0x00, 0x37, 0x00, 0x00, 0x00, 0x6c, 0x00, 0x40, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x00, 0x00, 0x00, 0x94, 0x1f, 0x04, 0x00, 0x04, 0x00, 0x5c, 
0x4d, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x04, 0x00, 0x03, 0x20, 0x40, 0x40, 0xff, 0x1f, 0xf9, 0xc0, 0x4d, 0x34, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x03, 0x20, 0x40, 0x40, 
0xfe, 0x1f, 0xf9, 0xc0, 0x4d, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x03, 0x20, 0x40, 0x40, 0xfd, 0x1f, 0xf9, 0xc0, 0x4d, 0x38, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 
0x03, 0x20, 0x45, 0x40, 0xfc, 0x1f, 0xf9, 0xc0, 0x00, 0x00, 0x00, 0x00};
unsigned char trama_LLC_24[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x78, 0xf0, 0xf0,
0x08, 0x08, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x85, 0x4f,
0xff, 0x53, 0x4d, 0x42, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0xc1, 0x1d, 0x00, 0x00, 0x01, 0x2a,
0x0e, 0x1a, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x88, 0x13, 0x00,
0x00, 0x00, 0x00, 0x1a, 0x00, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x27, 0x00, 0x5c,
0x50, 0x49, 0x50, 0x45, 0x5c, 0x4c, 0x41, 0x4e, 0x4d, 0x41, 0x4e, 0x00, 0x68, 0x00, 0x57, 0x72,
0x4c, 0x65, 0x68, 0x44, 0x4f, 0x00, 0x42, 0x31, 0x36, 0x42, 0x42, 0x44, 0x7a, 0x00, 0x01, 0x00,
0x00, 0x10, 0x02, 0x22, 0x00, 0x00};
unsigned char trama_LLC_25[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1,
0x01, 0x0a, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_26[250]={	0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0xbe, 0xf0, 0xf0,
0x08, 0x0a, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x4f, 0x85,
0xff, 0x53, 0x4d, 0x42, 0x25, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0xc1, 0x1d, 0x00, 0x00, 0x01, 0x2a,
0x0a, 0x08, 0x00, 0x6c, 0x00, 0x00, 0x00, 0x08, 0x00, 0x37, 0x00, 0x00, 0x00, 0x6c, 0x00, 0x40,
0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x00, 0x00, 0x00, 0x94, 0xbf, 0x04, 0x00, 0x04, 0x00, 0x5c,
0x4d, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x04, 0x00, 0x03, 0x20, 0x40, 0x40, 0xff, 0xbf, 0x29, 0xc8, 0x4d, 0x34, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x03, 0x20, 0x40, 0x40,
0xfe, 0xbf, 0x29, 0xc8, 0x4d, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x03, 0x20, 0x40, 0x40, 0xfd, 0xbf, 0x29, 0xc8, 0x4d, 0x38,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00,
0x03, 0x20, 0x45, 0x40, 0xfc, 0xbf, 0x29, 0xc8, 0x00, 0x00, 0x00, 0x00};
unsigned char trama_LLC_27[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x12, 0xf0, 0xf0, 
0x0a, 0x0b, 0x0e, 0x00, 0xff, 0xef, 0x14, 0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x85, 0x4f, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_28[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_29[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x0b, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_30[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1,
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_31[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x0b, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};	
unsigned char trama_LLC_32[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_33[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x35, 0xf0, 0xf0, 
0x0c, 0x0a, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x04, 0x00, 0x00, 0x00, 0x00, 0x28, 0x00, 0x85, 0x4f, 
0xff, 0x53, 0x4d, 0x42, 0x71, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x82, 0x07, 
0x00, 0x00, 0x00 };
unsigned char trama_LLC_34[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x35, 0xf0, 0xf0, 
0x0a, 0x0e, 0x0e, 0x00, 0xff, 0xef, 0x16, 0x0c, 0x00, 0x00, 0x28, 0x00, 0x28, 0x00, 0x4f, 0x85, 
0xff, 0x53, 0x4d, 0x42, 0x71, 0x00, 0x00, 0x00, 0x00, 0x80, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x82, 0x07, 
0x00, 0x00, 0x00};
unsigned char trama_LLC_35[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_36[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x0f, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_37[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x0f, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_38[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_39[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x12, 0xf0, 0xf0, 
0x0e, 0x0d, 0x0e, 0x00, 0xff, 0xef, 0x14, 0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x85, 0x4f, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_40[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x04, 0xf0, 0xf0, 
0x01, 0x0d, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_41[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x11, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_42[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x12, 0xf0, 0xf0, 
0x10, 0x0d, 0x0e, 0x00, 0xff, 0xef, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x85, 0x4f, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_43[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x04, 0xf0, 0xf1, 
0x01, 0x13, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_44[250]={0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x03, 0xf0, 0xf0, 
0x53, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};
unsigned char trama_LLC_45[250]={0x00, 0x00, 0xe8, 0x15, 0xbb, 0x75, 0x00, 0x20, 0x18, 0x66, 0xc6, 0x02, 0x00, 0x03, 0xf0, 0xf1, 
0x73, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 
0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20};

int ObtenerDatos(int descriptor_socket)
{
	struct ifreq nic;//nic es el nombre de la estructura ifreq
	int index, i;
	printf("\nInserta nombre de la interfaz: ");
	scanf("%s", nic.ifr_name);//guarda la cadena en ifr_name

	if(ioctl(descriptor_socket, SIOCGIFINDEX, &nic)==-1)//obtenemos el indice
	{
		perror("\nError al obtener el indice");
		exit(1);
	}
	else
	{
		index=nic.ifr_ifindex;

		if(ioctl(descriptor_socket, SIOCGIFHWADDR, &nic)==-1)//obtenemos la direccion MAC
		{
			perror("\nError al obtener la direccion MAC");
			exit(1);
		}
		else
		{
			memcpy(MACorigen, nic.ifr_hwaddr.sa_data+0, 6);//la direccion MAC se guardara en sa_data
			printf("\nDireccion MAC: ");
			for(i=0; i<6; i++)
				printf("%.2x:", MACorigen[i]);

			if(ioctl(descriptor_socket, SIOCGIFADDR, &nic)==-1)//obtenemos la direccion IP
			{
				perror("\nError al obtener la direccion IP");
				exit(1);
			}
			else
			{
				/*En este caso la direccion IP tambien se guardara dentro de nic.ifr_addr.sa_data pero desde el bit 2*/
				memcpy(IPorigen, nic.ifr_addr.sa_data+2, 4);//la direccion IP se guardara en sa_data
				printf("\nDireccion IP: ");
				for(i=0; i<4; i++)
					printf("%d.", IPorigen[i]);

                if(ioctl(descriptor_socket, SIOCGIFNETMASK, &nic)==-1)//obtenemos la mascara de subred
                {
                    perror("\nError al obtener la mascara de subred");
                    exit(1);
                }
                else
                {
                    /*En este caso la mascara de subred  se guardara dentro de sa_data pero desde la variable netmask y desde el
                    bit 2*/
                    memcpy(MascaraSubred, nic.ifr_netmask.sa_data+2, 4);//la mascara de subred se guardara en sa_data
                    printf("\nMascara de Subred: ");
                    for(i=0; i<4; i++)
                        printf("%d.", MascaraSubred[i]);

                    printf("\nFamilia: %.4x", nic.ifr_netmask.sa_family);
                    //obtenemos la familia de protocolos a la que pertenece la mascara de subred
                }
			}
		}
	}

return index;
}

void ImprimirTrama(unsigned char *trama, int tam)
{
	int i;

	for(i=0; i<tam; i++)
	{
		if(i%16==0)
			printf("\n");
		printf("%.2x", trama[i]);
	}
}

void EnviaTramaLLC(int descriptor_socket, int indice, unsigned char *trama)
{
	int tam;
	struct sockaddr_ll capaEnlace;
	memset(&capaEnlace, 0x00, sizeof(capaEnlace));
	capaEnlace.sll_family=AF_PACKET;
	capaEnlace.sll_protocol=htons(ETH_P_ALL);
	capaEnlace.sll_ifindex=indice;
	tam=sendto(descriptor_socket, trama, 60, 0, (struct sockaddr*)&capaEnlace, sizeof(capaEnlace));

	if(tam==-1)
	{
		perror("\nError al enviar trama");
		exit(1);
	}
	else
	{
		perror("\n\nExito al enviar trama");
		printf("\n----------Trama LLC enviada----------");
		ImprimirTrama(trama, tam);
	}
}

int main()
{
	int packet_socket, indice;
	packet_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));

	if(packet_socket==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	else
	{
		perror("\nExito al abrir el socket");
		indice=ObtenerDatos(packet_socket);//enviamos el descriptor de socket
		printf("\nEl indice es: %d \n", indice);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_1);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_2);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_3);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_4);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_5);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_6);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_7);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_8);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_9);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_10);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_11);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_12);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_13);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_14);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_15);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_16);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_17);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_18);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_19);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_20);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_21);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_22);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_23);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_24);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_25);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_26);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_27);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_28);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_29);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_30);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_31);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_32);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_33);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_34);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_35);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_36);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_37);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_38);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_39);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_40);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_41);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_42);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_43);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_44);
		EnviaTramaLLC(packet_socket, indice, trama_LLC_45);
	}

close(packet_socket);
return 0;
}