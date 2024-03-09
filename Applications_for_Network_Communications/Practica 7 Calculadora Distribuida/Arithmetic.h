/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#ifndef _ARITHMETIC_H_RPCGEN
#define _ARITHMETIC_H_RPCGEN

#include <rpc/rpc.h>


#ifdef __cplusplus
extern "C" {
#endif


struct operandos {
	float operando1;
	float operando2;
};
typedef struct operandos operandos;

#define ARITHMETIC_PRG 0x20000001
#define ARITHMETIC_VER 1

#if defined(__STDC__) || defined(__cplusplus)
#define suma 1
extern  float * suma_1(operandos *, CLIENT *);
extern  float * suma_1_svc(operandos *, struct svc_req *);
#define resta 2
extern  float * resta_1(operandos *, CLIENT *);
extern  float * resta_1_svc(operandos *, struct svc_req *);
#define multiplicacion 3
extern  float * multiplicacion_1(operandos *, CLIENT *);
extern  float * multiplicacion_1_svc(operandos *, struct svc_req *);
#define division 4
extern  float * division_1(operandos *, CLIENT *);
extern  float * division_1_svc(operandos *, struct svc_req *);
#define exponencial 5
extern  float * exponencial_1(operandos *, CLIENT *);
extern  float * exponencial_1_svc(operandos *, struct svc_req *);
extern int arithmetic_prg_1_freeresult (SVCXPRT *, xdrproc_t, caddr_t);

#else /* K&R C */
#define suma 1
extern  float * suma_1();
extern  float * suma_1_svc();
#define resta 2
extern  float * resta_1();
extern  float * resta_1_svc();
#define multiplicacion 3
extern  float * multiplicacion_1();
extern  float * multiplicacion_1_svc();
#define division 4
extern  float * division_1();
extern  float * division_1_svc();
#define exponencial 5
extern  float * exponencial_1();
extern  float * exponencial_1_svc();
extern int arithmetic_prg_1_freeresult ();
#endif /* K&R C */

/* the xdr functions */

#if defined(__STDC__) || defined(__cplusplus)
extern  bool_t xdr_operandos (XDR *, operandos*);

#else /* K&R C */
extern bool_t xdr_operandos ();

#endif /* K&R C */

#ifdef __cplusplus
}
#endif

#endif /* !_ARITHMETIC_H_RPCGEN */
