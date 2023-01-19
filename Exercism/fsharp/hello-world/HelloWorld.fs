module HelloWorld

// 2022Jan08 Sunday epj
//
// So, a typical HelloWorld program has to print something.
// The way the test infrastructure is set up, there's no actual call to
// any output function. The implementation simply makes an assignment to
// a variable, then the test suite checks the value. OK. :~}
//
// The test suite is small. Here's the whole thing:
//
//     module HelloWorldTests
// 
//     open FsUnit.Xunit
//     open Xunit
// 
//     open HelloWorld
// 
//     [<Fact>]
//     let ``Say Hi!`` () =
//         hello |> should equal "Hello, World!"
//
// That's not exactly intuitive.
// Short and sweet, yes, but not obvious syntax. Like, what is 'should'
// and 'equal' here? Is 'equal' a parameter to a should() call?
// TODO:
//  [ ] don't get wrapped around the axle on this 
//      [v] keep going
//      [v] submit the solution
//      [ ] passes locally, fails on server, waiting for mentor feedback
//      [ ] publish it
//      [ ] learn the F# langauge
//      [ ] come back to crafting your own unit tests and fully
//          understandin this test suite
//
//  [ ] read up on this whole FsUnit.Xunit business
//

// MENTORING
//  Hi. I dabbled with Exercism about two years ago. Recently completed
//  a few problems on the Python track. I am new to F#. I am *NOT* new
//  to either Python nor programming in general.
//
//  My test suite is actually passing locally. Here's the output:
//
// Eriks-Mac-mini:hello-world ejohnson$ dotnet test
//   Determining projects to restore...
//   All projects are up-to-date for restore.
//   HelloWorld -> /Users/ejohnson/src/git/programming/Exercism/fsharp/hello-world/bin/Debug/net7.0/HelloWorld.dll
// Test run for /Users/ejohnson/src/git/programming/Exercism/fsharp/hello-world/bin/Debug/net7.0/HelloWorld.dll (.NETCoreApp,Version=v7.0)
// Microsoft (R) Test Execution Command Line Tool Version 17.4.0 (x64)
// Copyright (c) Microsoft Corporation.  All rights reserved.
// 
// Starting test execution, please wait...
// A total of 1 test files matched the specified pattern.
// 
// Passed!  - Failed:     0, Passed:     1, Skipped:     0, Total:     1, Duration: < 1 ms - HelloWorld.dll (net7.0)
// 
// Hmmm, then something strange happened. After updating comments above,
// re-submitting my code so that any potential mentor would have that info,
// the submission then passed.
// Something is fishy about first submission, but I can't see anything
// wrong.


// THE SOLUTION
let hello = "Hello, World!"

// EOF

