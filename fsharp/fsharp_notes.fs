//       1         2         3         4         5         6         7         8
//345678901234567890123456789012345678901234567890123456789012345678901234567890

(*
                                F# NOTES
                                ========
2022Apr08
Notes for my F# adventure...

REFERENCES
----------------
PF3: "Using "Programming F# 3.0" 2E, Chris Smith, O'Reilly
FPwFS: "Functional Programming with F#", Yusuf Motara, eDoc
NB: My page citations are the PDF page, not necessarily the page number
    actually shown in the PDF document.

*)


//======================================================================
// Part 1 - how to get some code in the system and run something.

// 'dotnet' is the basic command to get stuff done.
> dotnet -h
// Will spew a fair amount of doc...

> dotnet fsi   // enter the interactive F# interpreter / REPL:

> #quit;;   // exit the interactive 'fsi' REPL


//
// run a simple F# script without compilation
//

// 1) put the following text into a file named 'hello.fsx'
printfn "Hello, World!"

// 2) Run it:
> dotnet fsi hello.fsx
Hello, World!
// SUCCESS!


New, full projects can be created with 'dotnet new ...'
There's two main ways to do that:
    1) convert the current directory into a project
        > dotnet new console -lang F#
    2) specify the name to create a new directory for the project
        > dotnet new console -lang F# -name myNewProj
        // see also -o option

You can get more help on 'dotnet new':
> dotnet new -h
> dotnet new console -h


//
// Create a new F# project (in the *CURRENT* directory)
//
> dotnet new console --language F#

This will generate a number of things in the current directory:

    Program.fs
    fsharp.fsproj
    obj/

As yet, this is not compiled, but you can still run it.
> dotnet run
Hello from F#

// SUCCESS! (print of boilerplate code that was in Program.fs)
// NB: my hello.fsx file is left untouched, still in
// this project directory, but now not really part of this project.

// We *can* build it...
C:\Users\ejohn\src\git\programming\fsharp>dotnet build
Microsoft (R) Build Engine version 17.1.0+ae57d105c for .NET
Copyright (C) Microsoft Corporation. All rights reserved.

  Determining projects to restore...
  All projects are up-to-date for restore.
  fsharp -> C:\Users\ejohn\src\git\programming\fsharp\bin\Debug\net6.0\fsharp.dll

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.06

>

A bin/ directory is added into this current project dir.
Dig down into it, and you can find a runnable: fsharp.exe
Modify the Program.fs code to say "Hello, F#!!!", rebuild, re-run .exe
to make sure we're really running what we think we're building:

C:\Users\ejohn\src\git\programming\fsharp\bin\Debug\net6.0>.\fsharp.exe
Hello, F#!!!
// Yes! Yes, we are.

// ej: I think it says 'fsharp' because that was the name of the
// directory I first used 'dotnet new' in, and that should really be in a
// subdirectory of my ~/src/git/programming/fsharp/ directory
// (or give -o option to specify output dir in orig dotnet new command)
// ej: Yes, that is a fact. Made new dir 'hello' within .../fsharp/ and
// hello.exe is what is created (under Debug/ ) after running.

// Build for production (from project home dir)
> dotnet publish
// This generates new stuff. What exactly the differences are, I am not
// sure (i.e., between the hello.exe here and the hello.exe in the
// directory above
// TODO: write a Python program to do the raw digging - what is the
// structure of this .exe?  What *IS* different? (debugging info
// stripped?)
C:\Users\ejohn\src\git\programming\fsharp\hello\bin\Debug\net6.0\publish>ls
FSharp.Core.dll  de  fr               hello.dll  hello.pdb                 it  ko  pt-BR  tr   zh-Hant
cs               es  hello.deps.json  hello.exe  hello.runtimeconfig.json  ja  pl  ru     zh-Hans

// Some sort of support for langauges here, though it is generating
// empty files. That's not all that helpful.  cs, de, es, fr, it, ja...
// all are size 0  (i.e., all files not starting "hello")


Ok, that's how to get some code slapped down and build a program from
it, run it as a stand-aone exe or invoke an .fsx file via:
> dotnet fsi myFilename.fsx


========================================================================
Part 2 - basic F# literals syntax, conversions, basic math functions


// copied from FP3 page 16
// ej: NB: 's' -> short, 'l' -> long

// Type     Suffix  .NET Type       Range
//--------  ------  -------------   --------------------------  
byte        uy      System.Byte     [0 .. 255]
sbyte       y       System.SByte    [-128 .. 127]
int16       s       System.Int16    [-32768 .. 32767]
uint16      us      System.UInt16   [0 .. 65535]
int, int32          System.Int32    [-2**31 .. 2**31-1]
uint32      u       System.UInt32   [0 .. 2**32-1]    
int64       L       System.Int64    [-2**63 .. 2**63-1]
uint64      UL      System.UInt64   [0 .. 2**64-1]
float               System.Double   IEEE 64 w/ ~15 sig. digits
float32     f       System.Single   IEEE 32 w/ ~7 sig. digits
decimal     M       System.Decimal  fixed precision float type w/ 28 sig digs (precisely)

// NB: int, int32 is default, no suffix to literals of that type

// You can specify literals in hex, octal, binary...
> let x = 0xbadcab;;
val x: int = 12246187

> let x = 0o77;;
val x: int = 63

> let binvar = 0b1111uy;;
val binvar: byte = 15uy

> let binvar = 0b1111y;;
val binvar: sbyte = 15y

> let binvar = 0b11111111y;;
val binvar: sbyte = -1y

> let binvar = 0b11111111uy;;
val binvar: byte = 255uy


// Unlike most languages, there is *NO* type coercion! It must all be
// explicit, but note that each of the types given above can be used as
// a conversion routine (each conversion routine supports all the other
// types)

> let x = 0b111uy;;
val x: byte = 7uy

> let y = 3;;
val y: int = 3

> x + y;;

  x + y
  ----^

stdin(10,5): error FS0001: The type 'int' does not match the type 'byte'

> int 0b1111uy + 10;;
val it: int = 25

> int 5.6;;
val it: int = 5


// note that conversion can lead to data loss, but this is not an error:
> byte 5555;;
val it: byte = 179uy

> 5555 % 256;;
val it: int = 179


F# supports the 4 standard math operators: +, -, *, /
Plus power and modulus: **, %
// NB!!!: ** operator only works on float and float32 - must either
// convert or use pown (below)

> 2.0 ** 8;;
val it: float = 256.0

And other built-in math functions (see pg 18)
abs, ceil, exp, floor, sign, log, log10, sqrt
cos, sing, tan
pown  // power of integer

> 2.0 ** 8;;
val it: float = 256.0

> 2.0 ** 8 = pown 2 8;;
val it: bool = true
// ej: WHOA... That's a bit unexpected - equality of different types
// despite being unable to combine types w/ standard operators!!
// This seems to be a special case of comparing a round float to its
// equivalent int value, and does not apply in general:

- 0b1111uy = 15;;

  0b1111uy = 15;;
  -----------^^

stdin(38,12): error FS0001: This expression was expected to have type
    'byte'
but here has type
    'int'

Bitwise Operators
-------------------
&&& And
||| Or
^^^ XOR
<<< Shift Left
>>> Shift Right

// examples...
> printf "%B " (0b1010 &&& 0b1100);;
1000 val it: unit = ()

> printf "%B " (0b1010 ||| 0b1100);;
1110 val it: unit = ()

> printf "%B " (0b1010 ^^^ 0b1100);;
110 val it: unit = ()


Boolean "operators" (they are really functions)
-------------------------------------------------
> [false && true; false || true; not false; not true];;
val it: bool list = [false; true; true; false]
// NB1: not the standard C "not" operator (~)!
// NB2: no native XOR

// As mentioned above, these are really functions:
> let f = (&&);;
val f: (bool -> bool -> bool)

> f true true;;
val it: bool = true

> f true false;;
val it: bool = false

// NB: page 23 gives a definition of a function for printing a truth table,
// then passes the operator/function in to it to print the truth table.

// NB: This are "short circuit" functions (as you would expect).


(* Strings
-----------
...work more or less as one probably expects (with a few exceptions) *)

// standard escapes
> let escapes = ['\'', '\"', '\\', '\b', '\n', '\r', '\t'];;
val escapes: (char * char * char * char * char * char * char) list =
  [('\'', '"', '\\', '\b', '\010', '\013', '\009')]

> let quote = "'Fuck!', Pooh said.";;
val quote: string = "'Fuck!', Pooh said."

// mutli-line strings without any special syntax:
> let mls = "This string
takes up
three lines.";;

// single quoting is used for characters, not for strings
> let s = 'foo';;

  let s = 'foo';;
  --------^

stdin(61,9): error FS0010: Unexpected quote symbol in binding

> let s = "foo";;
val s: string = "foo"


//======================================================================
// Core Types

// Unit (you can think of this as null or Python None, but it is
// distinct from an uninitialized value).
> let x = ();;
val x: unit = ()


Tuples
------------
> let x = 1,2;;
val x: int * int = (1, 2)

> let x = (1, 2);;
val x: int * int = (1, 2)

// tuple unpacking much like Python
> let x, y = "one", "two";;
val y: string = "two"
val x: string = "one"

// two special functions: fst, snd  // get first and second tuple elements
> let xy = 1,2;;
val xy: int * int = (1, 2)

> fst xy;;
val it: int = 1

> snd xy;;
val it: int = 2


List  (NB: ',' is not the element separator!)
-----------------------------------------------
> [1; 2; 3];;
val it: int list = [1; 2; 3]

// This is something distinctly different: a list of int 3-tuples
> [1,2,3];;
val it: (int * int * int) list = [(1, 2, 3)]


========================================================================
Lists (FP3, pg 34-42)
  basics, comprehensions, List module functions

//
// basics
//

// 'cons' operator: '::' - tack a new element on front of list
> let l1 = [1;2;3]
- let l2 = 0 :: l1
- l2;;
val l1: int list = [1; 2; 3]
val l2: int list = [0; 1; 2; 3]
val it: int list = [0; 1; 2; 3]

// index list elements as you would expect:
> l1[1];;
val it: int = 2

// ranges
> let x = [1..5];;
val x: int list = [1; 2; 3; 4; 5]

> let x = [10 .. -1 .. 0];;
val x: int list = [10; 9; 8; 7; 6; 5; 4; 3; 2; 1; 0]

// list concatenation w/ '@' operator
> let evens = [2..2..10]
- let odds = [1..2..10]
- let both = evens @ odds;;
val evens: int list = [2; 4; 6; 8; 10]
val odds: int list = [1; 3; 5; 7; 9]
val both: int list = [2; 4; 6; 8; 10; 1; 3; 5; 7; 9]

//
// List comprehension
//

// simple
let numsNear x = [
  yield x - 1
  yield x
  yield x + 1
]

> numsNear 3;;
val it: int list = [2; 3; 4]

// unlike Python, pretty much any valid F# code can go inside a List comprehension
> let x = [
  let negate x = -x
  for i in 1 .. 10 do 
    if i % 2 = 0 then
      yield negate i
    else
      yield i
];;
val x: int list = [1; -2; 3; -4; 5; -6; 7; -8; 9; -10]


//
// List module functions
// NB: List is a module in Microsoft.FSharp.Collections (automatically imported)
//

> List.length x;;
val it: int = 10

> List.head x;;
val it: int = 1

> List.tail x;;
val it: int list = [-2; 3; -4; 5; -6; 7; -8; 9; -10]

// List.exists:  apply pred func to list, true if any element meets pred.
// (like Python 'in')
> let has8 el = (el = 8)
- List.exists has8 x;;
val has8: el: int -> bool
val it: bool = false

> let has7 el = (el = 7)
- List.exists has7 x;;
val has7: el: int -> bool
val it: bool = true

// reverse
> List.rev x;;
val it: int list = [-10; 9; -8; 7; -6; 5; -4; 3; -2; 1]

// zip, map
> let i_l = [1..7]
- let sq i = i * i
- List.zip i_l (List.map sq i_l);;
val i_l: int list = [1; 2; 3; 4; 5; 6; 7]
val sq: i: int -> int
val it: (int * int) list =
  [(1, 1); (2, 4); (3, 9); (4, 16); (5, 25); (6, 36); (7, 49)]

// filter
> let even x = (x % 2 = 0)
- List.filter even [1..10];;
val even: x: int -> bool
val it: int list = [2; 4; 6; 8; 10]

// partition: ([elements where pred func true], [els w/ pred func false])
> List.partition even [1..10];;
val it: int list * int list = ([2; 4; 6; 8; 10], [1; 3; 5; 7; 9])

// List.reduce  (acc must be same type as list elements)
> List.reduce (+) [1..10];;
val it: int = 55

> List.reduce (*) [1..6];; 
val it: int = 720

// List.fold: a more general collapsing of lists where the type of list
//  element need not be related to the accumulator value.
// NB: the initiall acc value in the call
> let slen acc s = acc + String.length s  // acc function: old_acc one_elem -> new_acc_value
- let s_l = ["one"; "two"; "three"]       // list of strings to fold
- List.fold slen 0 s_l;;                  // squash the list down into one value: 11 total chars
val slen: acc: int -> s: string -> int
val s_l: string list = ["one"; "two"; "three"]
val it: int = 11

// sometimes list processing order doesn't matter, and sometimes it does
// (NB: .reduceBack and .foldBack are *NOT* just processing the reversed list!!!)
> let cat a b = a + b
- List.reduce cat ["a"; "b"; "c"];;
val cat: a: string -> b: string -> string
val it: string = "abc"

// you still get the same thing here
> let cat a b = a + b
- List.reduceBack cat ["a"; "b"; "c"];;
val cat: a: string -> b: string -> string
val it: string = "abc"

// because:  ("a" + "b") + "c" is same as: "a" + ("b" + "C")

// this happens to be true
> 4 - 3 - 2 - 1 = 1 - (2 - (3 - 4));;
val it: bool = true

// but working on the reverse list is *NOT* what's happening!!!
> 3 - 2 - 1 = 1 - (2 - 3);;
val it: bool = false

> let abc = ["a"; "b"; "c"];;
val abc: string list = ["a"; "b"; "c"]

> List.reduce cat (List.rev abc);;
val it: string = "cba"

> List.reduceBack cat abc;;
val it: string = "abc"

// List.map builds a new list under image of function
> let foo i = i + 42;;
val foo: i: int -> int

> List.map foo [1..5];;
val it: int list = [43; 44; 45; 46; 47]

// List.iter might seem like same thing, but it is not.
// It calls func for every element in list, bust expects a func that returns unit.
> List.iter foo [1..5];;
fsharp_notes.fs(138,11): error FS0001: Type mismatch. Expecting a
    'int -> unit'
but given a
    'int -> int'
The type 'unit' does not match the type 'int'

let foo i = printfn "::%d::" i
List.iter foo [1..3]

// EOF
