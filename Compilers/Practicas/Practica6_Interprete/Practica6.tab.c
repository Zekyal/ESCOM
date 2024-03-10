/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.5.1"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 9 "Practica6.y"

	#include <stdio.h>
	#include <stdlib.h>
	#include <math.h>
	#include <string.h>
	#include "Tabla_Simbolos.h"

	/* Variables auxiliares */
	tabla t;	// Declaracion de la tabla de Simbolos
	char buffer[50];	// Auxiliar para almacenar vcalores de variables
	int tipo;	//AUciliar para almacenar el tipo de dato de variables

	/* Mensajes de error */
	char* err_int_string = "Variable de tipo \"int\" requiere de valor de tipo entero, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_double_string = "Variable de tipo \"double\" requiere de valor de tipo decimal, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_string_int = "Variable de tipo \"string\" requiere de una cadena de texto, pero esta recibiendo un valor de tipo \"int\"\n";
	char* err_string_double = "Variable de tipo \"string\" requiere de una cadena de texto, pero esta recibiendo un valor de tipo \"double\"\n";
	char* err_opint_string = "Operacion de tipo \"int\" requiere de valores enteros, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_opdouble_string = "Operacion de tipo \"doubke\" requiere de valores enteros o decimales, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_pow_string = "Operacion POW con valo de tipo \"string\", requieren de un valor de tipo \"int\" como expoente\n";

	/* Declaracion de Funciones */
	char* Potencia_Cadena(char*, int);
	char* Invertir_Cadena(char*);

#line 96 "Practica6.tab.c"

# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Use api.header.include to #include this header
   instead of duplicating it here.  */
#ifndef YY_YY_PRACTICA6_TAB_H_INCLUDED
# define YY_YY_PRACTICA6_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ENTERO = 258,
    DECIMAL = 259,
    CADENA = 260,
    VARIABLE = 261,
    INT = 262,
    DOUBLE = 263,
    STRING = 264,
    POW = 265,
    NEGATIVO = 266,
    POSITIVO = 267
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 36 "Practica6.y"

	int entero;
	double decimal;
	char* cadena;

#line 167 "Practica6.tab.c"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_PRACTICA6_TAB_H_INCLUDED  */



#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))

/* Stored state numbers (used for stacks). */
typedef yytype_uint8 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && ! defined __ICC && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                            \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  2
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   377

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  24
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  8
/* YYNRULES -- Number of rules.  */
#define YYNRULES  81
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  163

#define YYUNDEFTOK  2
#define YYMAXUTOK   267


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
      19,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,    16,     2,     2,
      21,    23,    14,    12,    22,    13,     2,    15,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,    20,
       2,    11,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    17,    18
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint8 yyrline[] =
{
       0,    67,    67,    68,    71,    73,    74,    75,    77,    81,
      85,    91,    96,   102,   107,   113,   118,   119,   120,   121,
     123,   133,   143,   158,   159,   160,   161,   162,   163,   165,
     166,   168,   170,   171,   172,   173,   174,   175,   176,   177,
     178,   179,   180,   184,   185,   186,   187,   188,   189,   190,
     191,   192,   193,   194,   195,   196,   197,   198,   199,   201,
     202,   204,   205,   206,   208,   209,   210,   211,   212,   213,
     214,   215,   216,   217,   218,   221,   222,   224,   226,   227,
     230,   233
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "ENTERO", "DECIMAL", "CADENA",
  "VARIABLE", "INT", "DOUBLE", "STRING", "POW", "'='", "'+'", "'-'", "'*'",
  "'/'", "'%'", "NEGATIVO", "POSITIVO", "'\\n'", "';'", "'('", "','",
  "')'", "$accept", "input", "line", "expe", "expd", "expc", "dec", "ent", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_int16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,    61,    43,    45,    42,    47,    37,   266,   267,    10,
      59,    40,    44,    41
};
# endif

#define YYPACT_NINF (-11)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-1)

#define yytable_value_is_error(Yyn) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     -11,     2,   -11,   -11,   -11,   -11,   -10,    -3,    -2,    40,
      31,    92,    92,   -11,    38,   -11,   337,   345,   353,   -11,
     -11,    92,     5,    11,    36,    92,   -11,   -11,   361,   -11,
     -11,    39,    48,    92,    92,    92,    92,    92,   -11,    92,
      92,    92,    92,    92,   -11,    92,    92,    92,    92,    92,
     -11,   187,   238,   247,    92,    42,    92,    58,    92,    64,
     217,   222,   233,    38,   -11,     3,    35,    49,     3,    35,
      49,   -11,   -11,   -11,   -11,   -11,   -11,   -11,   -11,   -11,
       3,    35,    49,     3,    35,    49,   -11,   -11,   -11,   -11,
     -11,   -11,   -11,   -11,   -11,     3,    35,     3,    35,   -11,
     -11,   -11,   -11,   -11,   -11,    65,    66,    67,   256,   265,
     274,   -11,   283,   292,   301,   -11,   310,   319,   328,   -11,
      92,    92,    92,    68,   -11,   -11,   -11,    69,    73,    74,
      75,    79,    80,    84,    87,    88,    14,   136,   148,   153,
     165,   170,   182,   200,   205,   -11,   -11,   -11,   -11,   -11,
     -11,   -11,   -11,   -11,   -11,   -11,   -11,   -11,   -11,   -11,
     -11,   -11,   -11
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_int8 yydefact[] =
{
       2,     0,     1,    81,    80,    75,     0,     0,     0,     0,
       0,     0,     0,     4,     0,     3,     0,     0,     0,    43,
      23,     0,     0,     0,     0,     0,    30,    60,     0,    29,
      59,     0,     0,     0,     0,     0,     0,     0,     5,     0,
       0,     0,     0,     0,     6,     0,     0,     0,     0,     0,
       7,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    76,    24,    54,    32,    25,    55,
      33,    26,    56,    34,    27,    57,    35,    28,    58,    36,
      49,    44,    64,    50,    45,    65,    51,    46,    66,    52,
      47,    67,    53,    48,    68,    37,    69,    38,    70,    39,
      71,    40,    72,    41,    73,     0,     0,     0,     0,     0,
       0,     8,     0,     0,     0,     9,     0,     0,     0,    10,
       0,     0,     0,     0,    20,    21,    22,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    11,    12,    16,    14,    13,
      17,    18,    19,    15,    31,    63,    42,    62,    61,    74,
      77,    79,    78
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -11,   -11,   -11,    33,    89,    -1,   -11,   -11
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
      -1,     1,    15,    16,    17,    28,    19,    20
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_uint8 yytable[] =
{
      18,    21,     2,    22,    23,     3,     4,     5,     6,     7,
       8,     9,    10,    32,    11,    12,    54,    35,    36,    37,
      53,    13,    56,    14,    62,    55,    33,    34,    35,    36,
      37,    57,    67,    70,    73,    76,    79,   154,    82,    85,
      88,    91,    94,     5,    26,    29,    24,    58,    31,    41,
      42,    43,    25,   110,    51,   114,    59,   118,    60,    14,
      63,   111,   123,    47,    48,    49,    65,    68,    71,    74,
      77,    64,    80,    83,    86,    89,    92,   115,    95,    97,
      99,   101,   103,   119,   124,   125,   126,   108,   145,   112,
     122,   116,   146,   147,   148,     3,     4,     5,   149,   150,
      27,    30,    10,   151,    11,    12,   152,   153,     0,     0,
      52,     0,     0,    14,    61,     0,     0,     0,     0,   138,
     141,   144,    66,    69,    72,    75,    78,     0,    81,    84,
      87,    90,    93,     0,    96,    98,   100,   102,   104,     0,
       0,     0,     0,   109,     0,   113,     0,   117,    39,    40,
      41,    42,    43,   136,   139,   142,     0,     0,     0,   155,
      45,    46,    47,    48,    49,    33,    34,    35,    36,    37,
       0,   156,     0,     0,     0,     0,   157,    39,    40,    41,
      42,    43,    45,    46,    47,    48,    49,     0,   158,     0,
       0,     0,     0,   159,    33,    34,    35,    36,    37,    33,
      34,    35,    36,    37,     0,   160,     0,   105,     0,   137,
     140,   143,    39,    40,    41,    42,    43,    45,    46,    47,
      48,    49,     0,   161,     0,     0,     0,     0,   162,    33,
      34,    35,    36,    37,    39,    40,    41,    42,    43,   120,
       0,     0,     0,     0,   121,    45,    46,    47,    48,    49,
      39,    40,    41,    42,    43,   122,     0,     0,   106,    45,
      46,    47,    48,    49,     0,     0,     0,   107,    33,    34,
      35,    36,    37,     0,     0,     0,   127,    39,    40,    41,
      42,    43,     0,     0,     0,   128,    45,    46,    47,    48,
      49,     0,     0,     0,   129,    33,    34,    35,    36,    37,
       0,     0,     0,   130,    39,    40,    41,    42,    43,     0,
       0,     0,   131,    45,    46,    47,    48,    49,     0,     0,
       0,   132,    33,    34,    35,    36,    37,     0,     0,     0,
     133,    39,    40,    41,    42,    43,     0,     0,     0,   134,
      45,    46,    47,    48,    49,     0,     0,     0,   135,    33,
      34,    35,    36,    37,     0,     0,    38,    39,    40,    41,
      42,    43,     0,     0,    44,    45,    46,    47,    48,    49,
       0,     0,    50,    45,    46,    47,    48,    49
};

static const yytype_int8 yycheck[] =
{
       1,    11,     0,     6,     6,     3,     4,     5,     6,     7,
       8,     9,    10,    14,    12,    13,    11,    14,    15,    16,
      21,    19,    11,    21,    25,    20,    12,    13,    14,    15,
      16,    20,    33,    34,    35,    36,    37,    23,    39,    40,
      41,    42,    43,     5,    11,    12,     6,    11,    10,    14,
      15,    16,    21,    54,    21,    56,    20,    58,    25,    21,
      21,    19,    63,    14,    15,    16,    33,    34,    35,    36,
      37,    23,    39,    40,    41,    42,    43,    19,    45,    46,
      47,    48,    49,    19,    19,    19,    19,    54,    19,    56,
      22,    58,    19,    19,    19,     3,     4,     5,    19,    19,
      11,    12,    10,    19,    12,    13,    19,    19,    -1,    -1,
      21,    -1,    -1,    21,    25,    -1,    -1,    -1,    -1,   120,
     121,   122,    33,    34,    35,    36,    37,    -1,    39,    40,
      41,    42,    43,    -1,    45,    46,    47,    48,    49,    -1,
      -1,    -1,    -1,    54,    -1,    56,    -1,    58,    12,    13,
      14,    15,    16,   120,   121,   122,    -1,    -1,    -1,    23,
      12,    13,    14,    15,    16,    12,    13,    14,    15,    16,
      -1,    23,    -1,    -1,    -1,    -1,    23,    12,    13,    14,
      15,    16,    12,    13,    14,    15,    16,    -1,    23,    -1,
      -1,    -1,    -1,    23,    12,    13,    14,    15,    16,    12,
      13,    14,    15,    16,    -1,    23,    -1,    20,    -1,   120,
     121,   122,    12,    13,    14,    15,    16,    12,    13,    14,
      15,    16,    -1,    23,    -1,    -1,    -1,    -1,    23,    12,
      13,    14,    15,    16,    12,    13,    14,    15,    16,    22,
      -1,    -1,    -1,    -1,    22,    12,    13,    14,    15,    16,
      12,    13,    14,    15,    16,    22,    -1,    -1,    20,    12,
      13,    14,    15,    16,    -1,    -1,    -1,    20,    12,    13,
      14,    15,    16,    -1,    -1,    -1,    20,    12,    13,    14,
      15,    16,    -1,    -1,    -1,    20,    12,    13,    14,    15,
      16,    -1,    -1,    -1,    20,    12,    13,    14,    15,    16,
      -1,    -1,    -1,    20,    12,    13,    14,    15,    16,    -1,
      -1,    -1,    20,    12,    13,    14,    15,    16,    -1,    -1,
      -1,    20,    12,    13,    14,    15,    16,    -1,    -1,    -1,
      20,    12,    13,    14,    15,    16,    -1,    -1,    -1,    20,
      12,    13,    14,    15,    16,    -1,    -1,    -1,    20,    12,
      13,    14,    15,    16,    -1,    -1,    19,    12,    13,    14,
      15,    16,    -1,    -1,    19,    12,    13,    14,    15,    16,
      -1,    -1,    19,    12,    13,    14,    15,    16
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_int8 yystos[] =
{
       0,    25,     0,     3,     4,     5,     6,     7,     8,     9,
      10,    12,    13,    19,    21,    26,    27,    28,    29,    30,
      31,    11,     6,     6,     6,    21,    27,    28,    29,    27,
      28,    10,    29,    12,    13,    14,    15,    16,    19,    12,
      13,    14,    15,    16,    19,    12,    13,    14,    15,    16,
      19,    27,    28,    29,    11,    20,    11,    20,    11,    20,
      27,    28,    29,    21,    23,    27,    28,    29,    27,    28,
      29,    27,    28,    29,    27,    28,    29,    27,    28,    29,
      27,    28,    29,    27,    28,    29,    27,    28,    29,    27,
      28,    29,    27,    28,    29,    27,    28,    27,    28,    27,
      28,    27,    28,    27,    28,    20,    20,    20,    27,    28,
      29,    19,    27,    28,    29,    19,    27,    28,    29,    19,
      22,    22,    22,    29,    19,    19,    19,    20,    20,    20,
      20,    20,    20,    20,    20,    20,    27,    28,    29,    27,
      28,    29,    27,    28,    29,    19,    19,    19,    19,    19,
      19,    19,    19,    19,    23,    23,    23,    23,    23,    23,
      23,    23,    23
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_int8 yyr1[] =
{
       0,    24,    25,    25,    26,    26,    26,    26,    26,    26,
      26,    26,    26,    26,    26,    26,    26,    26,    26,    26,
      26,    26,    26,    27,    27,    27,    27,    27,    27,    27,
      27,    27,    27,    27,    27,    27,    27,    27,    27,    27,
      27,    27,    27,    28,    28,    28,    28,    28,    28,    28,
      28,    28,    28,    28,    28,    28,    28,    28,    28,    28,
      28,    28,    28,    28,    28,    28,    28,    28,    28,    28,
      28,    28,    28,    28,    28,    29,    29,    29,    29,    29,
      30,    31
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     2,     2,     2,     4,     4,
       4,     6,     6,     6,     6,     6,     6,     6,     6,     6,
       5,     5,     5,     1,     3,     3,     3,     3,     3,     2,
       2,     6,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     6,     1,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     2,
       2,     6,     6,     6,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     6,     1,     3,     6,     6,     6,
       1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YYUSE (yyoutput);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyo, yytoknum[yytype], *yyvaluep);
# endif
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyo, yytype, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[+yyssp[yyi + 1 - yynrhs]],
                       &yyvsp[(yyi + 1) - (yynrhs)]
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen(S) (YY_CAST (YYPTRDIFF_T, strlen (S)))
#  else
/* Return the length of YYSTR.  */
static YYPTRDIFF_T
yystrlen (const char *yystr)
{
  YYPTRDIFF_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYPTRDIFF_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYPTRDIFF_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            else
              goto append;

          append:
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (yyres)
    return yystpcpy (yyres, yystr) - yyres;
  else
    return yystrlen (yystr);
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYPTRDIFF_T *yymsg_alloc, char **yymsg,
                yy_state_t *yyssp, int yytoken)
{
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat: reported tokens (one for the "unexpected",
     one per "expected"). */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Actual size of YYARG. */
  int yycount = 0;
  /* Cumulated lengths of YYARG.  */
  YYPTRDIFF_T yysize = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[+*yyssp];
      YYPTRDIFF_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
      yysize = yysize0;
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYPTRDIFF_T yysize1
                    = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
                    yysize = yysize1;
                  else
                    return 2;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
    default: /* Avoid compiler warnings. */
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    /* Don't count the "%s"s in the final size, but reserve room for
       the terminator.  */
    YYPTRDIFF_T yysize1 = yysize + (yystrlen (yyformat) - 2 * yycount) + 1;
    if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
      yysize = yysize1;
    else
      return 2;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          ++yyp;
          ++yyformat;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss;
    yy_state_t *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYPTRDIFF_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYPTRDIFF_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    goto yyexhaustedlab;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
# undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 4:
#line 71 "Practica6.y"
                {printf("Salto de Linea");}
#line 1480 "Practica6.tab.c"
    break;

  case 5:
#line 73 "Practica6.y"
                                {printf("\n\t->Resultado: %d\n\n", (yyvsp[-1].entero));}
#line 1486 "Practica6.tab.c"
    break;

  case 6:
#line 74 "Practica6.y"
                                {printf("\n\t->Resultado: %f\n\n", (yyvsp[-1].decimal));}
#line 1492 "Practica6.tab.c"
    break;

  case 7:
#line 75 "Practica6.y"
                                {printf("\n\t->Resultado: %s\n\n", (yyvsp[-1].cadena));}
#line 1498 "Practica6.tab.c"
    break;

  case 8:
#line 77 "Practica6.y"
                                                {
										Declaracion_variable(&t, (yyvsp[-2].cadena), 1, "0"); 
										Imprimir_Tabla(&t);
									}
#line 1507 "Practica6.tab.c"
    break;

  case 9:
#line 81 "Practica6.y"
                                                {
										Declaracion_variable(&t, (yyvsp[-2].cadena), 2, "0.0"); 
										Imprimir_Tabla(&t);
									}
#line 1516 "Practica6.tab.c"
    break;

  case 10:
#line 85 "Practica6.y"
                                                {
										Declaracion_variable(&t, (yyvsp[-2].cadena), 3, "(null)"); 
										Imprimir_Tabla(&t);
									}
#line 1525 "Practica6.tab.c"
    break;

  case 11:
#line 91 "Practica6.y"
                                                        {
												sprintf(buffer, "%d", (yyvsp[-2].entero)); 
												Declaracion_variable(&t, (yyvsp[-4].cadena), 1, buffer);
												Imprimir_Tabla(&t);
											}
#line 1535 "Practica6.tab.c"
    break;

  case 12:
#line 96 "Practica6.y"
                                                        {
												sprintf(buffer, "%lf", (yyvsp[-2].decimal));
												Declaracion_variable(&t, (yyvsp[-4].cadena), 1, buffer);
												Imprimir_Tabla(&t);
											}
#line 1545 "Practica6.tab.c"
    break;

  case 13:
#line 102 "Practica6.y"
                                                        {
												sprintf(buffer, "%lf", (yyvsp[-2].decimal)); 
												Declaracion_variable(&t, (yyvsp[-4].cadena), 2, buffer); 
												Imprimir_Tabla(&t);
											}
#line 1555 "Practica6.tab.c"
    break;

  case 14:
#line 107 "Practica6.y"
                                                        {
												sprintf(buffer, "%d", (yyvsp[-2].entero)); 
												Declaracion_variable(&t, (yyvsp[-4].cadena), 2, buffer); 
												Imprimir_Tabla(&t);
											}
#line 1565 "Practica6.tab.c"
    break;

  case 15:
#line 113 "Practica6.y"
                                                        {	
												Declaracion_variable(&t, (yyvsp[-4].cadena), 3, (yyvsp[-2].cadena)); 
												Imprimir_Tabla(&t);
											}
#line 1574 "Practica6.tab.c"
    break;

  case 16:
#line 118 "Practica6.y"
                                                        {	yyerror (err_int_string);	}
#line 1580 "Practica6.tab.c"
    break;

  case 17:
#line 119 "Practica6.y"
                                                        {	yyerror (err_double_string);	}
#line 1586 "Practica6.tab.c"
    break;

  case 18:
#line 120 "Practica6.y"
                                                        {	yyerror (err_string_int);	}
#line 1592 "Practica6.tab.c"
    break;

  case 19:
#line 121 "Practica6.y"
                                                        {	yyerror (err_string_double);	}
#line 1598 "Practica6.tab.c"
    break;

  case 20:
#line 123 "Practica6.y"
                                                {
											tipo = Tipo_Dato(&t, (yyvsp[-4].cadena));
											if (tipo ==1 || tipo == 2){
												sprintf(buffer, "%d", (yyvsp[-2].entero));
												Asignacion_variable(&t, (yyvsp[-4].cadena), tipo, buffer);
												Imprimir_Tabla(&t);
											}
											if (tipo == 3)
												yyerror(err_string_int);
										}
#line 1613 "Practica6.tab.c"
    break;

  case 21:
#line 133 "Practica6.y"
                                                {
											tipo = Tipo_Dato(&t, (yyvsp[-4].cadena));
											if (tipo ==1 || tipo == 2){
												sprintf(buffer, "%lf", (yyvsp[-2].decimal)); 
												Asignacion_variable(&t, (yyvsp[-4].cadena), tipo, buffer);
												Imprimir_Tabla(&t);
											}
											if (tipo == 3)
												yyerror(err_string_double);
										}
#line 1628 "Practica6.tab.c"
    break;

  case 22:
#line 143 "Practica6.y"
                                                {
											tipo = Tipo_Dato(&t, (yyvsp[-4].cadena));
											if (tipo ==1)
												yyerror(err_int_string);
											if (tipo == 2)
												yyerror(err_double_string);
											if (tipo == 3){
												Asignacion_variable(&t, (yyvsp[-4].cadena), tipo, (yyvsp[-2].cadena));
												Imprimir_Tabla(&t);
											}
										}
#line 1644 "Practica6.tab.c"
    break;

  case 23:
#line 158 "Practica6.y"
                        {(yyval.entero) = (yyvsp[0].entero);}
#line 1650 "Practica6.tab.c"
    break;

  case 24:
#line 159 "Practica6.y"
                                        {(yyval.entero) = (yyvsp[-2].entero) + (yyvsp[0].entero);}
#line 1656 "Practica6.tab.c"
    break;

  case 25:
#line 160 "Practica6.y"
                                        {(yyval.entero) = (yyvsp[-2].entero) - (yyvsp[0].entero);}
#line 1662 "Practica6.tab.c"
    break;

  case 26:
#line 161 "Practica6.y"
                                        {(yyval.entero) = (yyvsp[-2].entero) * (yyvsp[0].entero);}
#line 1668 "Practica6.tab.c"
    break;

  case 27:
#line 162 "Practica6.y"
                                        {(yyval.entero) = (yyvsp[-2].entero) / (yyvsp[0].entero);}
#line 1674 "Practica6.tab.c"
    break;

  case 28:
#line 163 "Practica6.y"
                                        {(yyval.entero) = (yyvsp[-2].entero) % (yyvsp[0].entero);}
#line 1680 "Practica6.tab.c"
    break;

  case 29:
#line 165 "Practica6.y"
                                                {(yyval.entero) = -(yyvsp[0].entero);}
#line 1686 "Practica6.tab.c"
    break;

  case 30:
#line 166 "Practica6.y"
                                                {(yyval.entero) = +(yyvsp[0].entero);}
#line 1692 "Practica6.tab.c"
    break;

  case 31:
#line 168 "Practica6.y"
                                                {(yyval.entero) = pow((yyvsp[-3].entero), (yyvsp[-1].entero));}
#line 1698 "Practica6.tab.c"
    break;

  case 32:
#line 170 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1704 "Practica6.tab.c"
    break;

  case 33:
#line 171 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1710 "Practica6.tab.c"
    break;

  case 34:
#line 172 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1716 "Practica6.tab.c"
    break;

  case 35:
#line 173 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1722 "Practica6.tab.c"
    break;

  case 36:
#line 174 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1728 "Practica6.tab.c"
    break;

  case 37:
#line 175 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1734 "Practica6.tab.c"
    break;

  case 38:
#line 176 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1740 "Practica6.tab.c"
    break;

  case 39:
#line 177 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1746 "Practica6.tab.c"
    break;

  case 40:
#line 178 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1752 "Practica6.tab.c"
    break;

  case 41:
#line 179 "Practica6.y"
                                        {yyerror(err_opint_string);}
#line 1758 "Practica6.tab.c"
    break;

  case 42:
#line 180 "Practica6.y"
                                                {yyerror(err_opint_string);}
#line 1764 "Practica6.tab.c"
    break;

  case 43:
#line 184 "Practica6.y"
                {(yyval.decimal) = (yyvsp[0].decimal);}
#line 1770 "Practica6.tab.c"
    break;

  case 44:
#line 185 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) + (yyvsp[0].decimal);}
#line 1776 "Practica6.tab.c"
    break;

  case 45:
#line 186 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) - (yyvsp[0].decimal);}
#line 1782 "Practica6.tab.c"
    break;

  case 46:
#line 187 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) * (yyvsp[0].decimal);}
#line 1788 "Practica6.tab.c"
    break;

  case 47:
#line 188 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) / (yyvsp[0].decimal);}
#line 1794 "Practica6.tab.c"
    break;

  case 48:
#line 189 "Practica6.y"
                                        {(yyval.decimal) = fmod((yyvsp[-2].decimal), (yyvsp[0].decimal));}
#line 1800 "Practica6.tab.c"
    break;

  case 49:
#line 190 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) + (yyvsp[0].entero);}
#line 1806 "Practica6.tab.c"
    break;

  case 50:
#line 191 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) - (yyvsp[0].entero);}
#line 1812 "Practica6.tab.c"
    break;

  case 51:
#line 192 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) * (yyvsp[0].entero);}
#line 1818 "Practica6.tab.c"
    break;

  case 52:
#line 193 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].decimal) / (yyvsp[0].entero);}
#line 1824 "Practica6.tab.c"
    break;

  case 53:
#line 194 "Practica6.y"
                                        {(yyval.decimal) = fmod((yyvsp[-2].decimal), (yyvsp[0].entero));}
#line 1830 "Practica6.tab.c"
    break;

  case 54:
#line 195 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].entero) + (yyvsp[0].decimal);}
#line 1836 "Practica6.tab.c"
    break;

  case 55:
#line 196 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].entero) - (yyvsp[0].decimal);}
#line 1842 "Practica6.tab.c"
    break;

  case 56:
#line 197 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].entero) * (yyvsp[0].decimal);}
#line 1848 "Practica6.tab.c"
    break;

  case 57:
#line 198 "Practica6.y"
                                        {(yyval.decimal) = (yyvsp[-2].entero) / (yyvsp[0].decimal);}
#line 1854 "Practica6.tab.c"
    break;

  case 58:
#line 199 "Practica6.y"
                                        {(yyval.decimal) = fmod((yyvsp[-2].entero), (yyvsp[0].decimal));}
#line 1860 "Practica6.tab.c"
    break;

  case 59:
#line 201 "Practica6.y"
                                                {(yyval.decimal) = -(yyvsp[0].decimal);}
#line 1866 "Practica6.tab.c"
    break;

  case 60:
#line 202 "Practica6.y"
                                                {(yyval.decimal) = +(yyvsp[0].decimal);}
#line 1872 "Practica6.tab.c"
    break;

  case 61:
#line 204 "Practica6.y"
                                                {(yyval.decimal) = pow((yyvsp[-3].decimal), (yyvsp[-1].decimal));}
#line 1878 "Practica6.tab.c"
    break;

  case 62:
#line 205 "Practica6.y"
                                                {(yyval.decimal) = pow((yyvsp[-3].decimal), (yyvsp[-1].entero));}
#line 1884 "Practica6.tab.c"
    break;

  case 63:
#line 206 "Practica6.y"
                                                {(yyval.decimal) = pow((yyvsp[-3].entero), (yyvsp[-1].decimal));}
#line 1890 "Practica6.tab.c"
    break;

  case 64:
#line 208 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1896 "Practica6.tab.c"
    break;

  case 65:
#line 209 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1902 "Practica6.tab.c"
    break;

  case 66:
#line 210 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1908 "Practica6.tab.c"
    break;

  case 67:
#line 211 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1914 "Practica6.tab.c"
    break;

  case 68:
#line 212 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1920 "Practica6.tab.c"
    break;

  case 69:
#line 213 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1926 "Practica6.tab.c"
    break;

  case 70:
#line 214 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1932 "Practica6.tab.c"
    break;

  case 71:
#line 215 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1938 "Practica6.tab.c"
    break;

  case 72:
#line 216 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1944 "Practica6.tab.c"
    break;

  case 73:
#line 217 "Practica6.y"
                                        {yyerror(err_opdouble_string);}
#line 1950 "Practica6.tab.c"
    break;

  case 74:
#line 218 "Practica6.y"
                                                {yyerror(err_opdouble_string);}
#line 1956 "Practica6.tab.c"
    break;

  case 75:
#line 221 "Practica6.y"
                {(yyval.cadena) = (yyvsp[0].cadena);}
#line 1962 "Practica6.tab.c"
    break;

  case 76:
#line 222 "Practica6.y"
                                {(yyval.cadena) = (yyvsp[-1].cadena);}
#line 1968 "Practica6.tab.c"
    break;

  case 77:
#line 224 "Practica6.y"
                                                {(yyval.cadena) = Potencia_Cadena((yyvsp[-3].cadena), (yyvsp[-1].entero));}
#line 1974 "Practica6.tab.c"
    break;

  case 78:
#line 226 "Practica6.y"
                                                {yyerror(err_pow_string);}
#line 1980 "Practica6.tab.c"
    break;

  case 79:
#line 227 "Practica6.y"
                                                {yyerror(err_pow_string);}
#line 1986 "Practica6.tab.c"
    break;

  case 80:
#line 230 "Practica6.y"
                {(yyval.decimal) = (yyvsp[0].decimal);}
#line 1992 "Practica6.tab.c"
    break;

  case 81:
#line 233 "Practica6.y"
                {(yyval.entero) = (yyvsp[0].entero);}
#line 1998 "Practica6.tab.c"
    break;


#line 2002 "Practica6.tab.c"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = YY_CAST (char *, YYSTACK_ALLOC (YY_CAST (YYSIZE_T, yymsg_alloc)));
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;


#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif


/*-----------------------------------------------------.
| yyreturn -- parsing is finished, return the result.  |
`-----------------------------------------------------*/
yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[+*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 237 "Practica6.y"


int main(){
	Inicializar_Tabla(&t);
	yyparse();
	Destruir_Tabla(&t);
}

yyerror (char *s){
	printf("ERROR: %s\n", s);
}

int yywrap(){
	return 1;
}

/*
	FUNCION POTENCIA CADENA

	-> Descripcion: Realiza la Opreacion POW con cadenas de texto
	-> Recibe: La cadena de texto a potenciar
	-> Devuelve: Cadena de texto potenciada
*/
char* Potencia_Cadena(char* cadena, int exponente){
	int size = strlen(cadena) * abs(exponente);
	char* resultado = (char*) malloc(size * sizeof(char));

	// Si el exponente es igual a cero, se devuelve una cadena vacia
	if(exponente == 0)
		resultado = "";
	// Si el exponente es mayor a cero, se devuelve la cadena replicada tantas
	// veces como lo indique el exponente
	if (exponente > 0){
		for(int i=0; i<exponente; i++)
			resultado = strcat(resultado, cadena);
	}
	// Si el exponente es menor a cero, se devuelve la cadena invertida replicada 
	// tantas veces como lo indique el exponente
	if (exponente < 0){
		char* cadena_invertida = Invertir_Cadena(cadena);

		for(int i=0; i<abs(exponente); i++)
			resultado = strcat(resultado, cadena_invertida);
	}

	return resultado;
}

/*
	FUNCION INVERTIR CADENA

	-> Descripcion: Invierte una Cadena
	-> Recibe: La cadena de texto a invertir
	-> Devuelve: Cadena de texto invertida
*/
char* Invertir_Cadena(char* cadena){
	int size = strlen(cadena);
	int j = size - 1;
	char* resultado = (char*) malloc(strlen(cadena) * sizeof(char));

	for(int i=0; i<size; i++){
		resultado[i] = cadena[j];
		j--;
	}

	return resultado;
}
