	.file	"Bubble_Sort.c"
	.comm	_numeros, 200, 5
	.text
	.globl	_llenar
	.def	_llenar;	.scl	2;	.type	32;	.endef
_llenar:
LFB15:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$0, (%esp)
	call	_time
	movl	%eax, (%esp)
	call	_srand
	movl	$0, -12(%ebp)
	jmp	L2
L3:
	call	_rand
	movl	%eax, %edx
	movl	-12(%ebp), %eax
	movl	%edx, _numeros(,%eax,4)
	addl	$1, -12(%ebp)
L2:
	cmpl	$49, -12(%ebp)
	jle	L3
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE15:
	.section .rdata,"dr"
LC0:
	.ascii "(%d) %d |\0"
LC1:
	.ascii "\12\0"
	.text
	.globl	_imprimir
	.def	_imprimir;	.scl	2;	.type	32;	.endef
_imprimir:
LFB16:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$0, -12(%ebp)
	jmp	L5
L6:
	movl	$49, %eax
	subl	-12(%ebp), %eax
	movl	_numeros(,%eax,4), %eax
	movl	%eax, 8(%esp)
	movl	-12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	addl	$1, -12(%ebp)
L5:
	cmpl	$49, -12(%ebp)
	jle	L6
	movl	$LC1, (%esp)
	call	_puts
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE16:
	.globl	_burbuja
	.def	_burbuja;	.scl	2;	.type	32;	.endef
_burbuja:
LFB17:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	$0, -4(%ebp)
	jmp	L8
L12:
	movl	$0, -8(%ebp)
	jmp	L9
L11:
	movl	-8(%ebp), %eax
	movl	_numeros(,%eax,4), %edx
	movl	-8(%ebp), %eax
	addl	$1, %eax
	movl	_numeros(,%eax,4), %eax
	cmpl	%eax, %edx
	jge	L10
	movl	-8(%ebp), %eax
	movl	_numeros(,%eax,4), %eax
	movl	%eax, -12(%ebp)
	movl	-8(%ebp), %eax
	addl	$1, %eax
	movl	_numeros(,%eax,4), %edx
	movl	-8(%ebp), %eax
	movl	%edx, _numeros(,%eax,4)
	movl	-8(%ebp), %eax
	leal	1(%eax), %edx
	movl	-12(%ebp), %eax
	movl	%eax, _numeros(,%edx,4)
L10:
	addl	$1, -8(%ebp)
L9:
	cmpl	$49, -8(%ebp)
	jle	L11
	addl	$1, -4(%ebp)
L8:
	cmpl	$49, -4(%ebp)
	jle	L12
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE17:
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB18:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	call	___main
	call	_llenar
	call	_imprimir
	call	_burbuja
	call	_imprimir
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE18:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_time;	.scl	2;	.type	32;	.endef
	.def	_srand;	.scl	2;	.type	32;	.endef
	.def	_rand;	.scl	2;	.type	32;	.endef
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_puts;	.scl	2;	.type	32;	.endef
