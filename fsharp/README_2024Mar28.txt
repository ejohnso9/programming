

2026Sep09
----------
[ ] Follow the MS tutorial at:
    https://dotnet.microsoft.com/en-us/learn/languages/fsharp-hello-world-tutorial/create


2024Mar28
----------

$ dotnet new console -lang F# -o MyFSharpApp
The template "Console App" was created successfully.

Processing post-creation actions...
Restoring C:\Users\ejohnson\src\fsharp\MyFSharpApp\MyFSharpApp.fsproj:
  Determining projects to restore...
  Restored C:\Users\ejohnson\src\fsharp\MyFSharpApp\MyFSharpApp.fsproj (in 828 ms).
Restore succeeded.


under the MyFSharpApp is the main source file: Program.fs
It should already contain something like:

// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"


Change the text if you want. Then, from within that dir:

> dotnet run
(* # SUCCESS!!!! *)


Change Program.fs source to:

// Define a new function
let printGreeting name =
    printfn $"Greetings from F#, {name}!"

// Call the new function
printGreeting "ej"   (* could also be: prinrtGreeting("ej") *)


> dotnet run     // Success a second time!

Need to continue here:
https://dotnet.microsoft.com/en-us/learn/languages/fsharp-hello-world-tutorial/next



You can also put code in a *.fsx file to run w/o compilation:

$ cat hello.fsx
// For more information see https://aka.ms/fsharp-console-apps

// Define a new function
let printGreeting name =
    printfn $"Greetings from F#, {name}!"

// Call the new function
printGreeting "ej"


RHINOCORPS+ejohnson@DESKTOP-VQVD8UM MINGW64 ~/src/fsharp/MyFSharpApp
$ dotnet fsi hello.fsx
Greetings from F#, ej!

(* EOF *)

