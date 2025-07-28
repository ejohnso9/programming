module LuciansLusciousLasagna

(*
AUTHOR
    Erik Johnson

DESCRIPTION
    Solution to Exercism problem: 
    https://exercism.org/tracks/fsharp/exercises/lucians-luscious-lasagna

HISTORY
--------
2023Jan10 ej created
2024Aug27 ej updating comments, revisiting this whole FS thing
             retest via:  $ dotnet test  // STILL PASSING

(base) Eriks-Mac-mini:lucians-luscious-lasagna ejohnson$ dotnet test
  Determining projects to restore...
  All projects are up-to-date for restore.
  LuciansLusciousLasagna -> /Users/ejohnson/src/git/programming/Exercism/fsharp/lucians-luscious-lasagna/bin/Debug/net7.0/LuciansLusciousLasagna.dll
Test run for /Users/ejohnson/src/git/programming/Exercism/fsharp/lucians-luscious-lasagna/bin/Debug/net7.0/LuciansLusciousLasagna.dll (.NETCoreApp,Version=v7.0)
Microsoft (R) Test Execution Command Line Tool Version 17.4.0 (x64)
Copyright (c) Microsoft Corporation.  All rights reserved.

Starting test execution, please wait...
A total of 1 test files matched the specified pattern.

Passed!  - Failed:     0, Passed:     6, Skipped:     0, Total:     6, Duration: 7 ms - LuciansLusciousLasagna.dll (net7.0)

*)


// define the 'expectedMinutesInOven' binding
let expectedMinutesInOven = 40

// define the 'remainingMinutesInOven' function
let remainingMinutesInOven bakedMin =
    expectedMinutesInOven - bakedMin

// define the 'preparationTimeInMinutes' function
let preparationTimeInMinutes nLayers =
    nLayers * 2

// define the 'elapsedTimeInMinutes' function
let elapsedTimeInMinutes nLayers bakedMin =
    preparationTimeInMinutes(nLayers) + bakedMin

