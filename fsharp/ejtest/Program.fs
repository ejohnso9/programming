// For more information see https://aka.ms/fsharp-console-apps


//         0123456789012
let log_s = "[WARNING]   Watch out: this has extra whitespace!"

let rec findBracket (s: string) (idx: int) =
    if s[idx] = ']' then idx else findBracket s (idx + 1)

let isWhite (c: char) =
    c = ' ' || c = '\n' || c = '\t' || c = '\f' || c = '\b' || c = '\r'

// let trimWsOffEnd =

let rec nextNonWhite (s: string) (idx: int) =
    if isWhite s[idx] then
        nextNonWhite s (idx + 1)
    else
        idx
    
let message log_line =
    let b_idx = findBracket log_s 0
    let nextNwIdx = nextNonWhite log_s (b_idx + 1)

printfn "first nonWhite after %d is %d" b_idx nextNwIdx 

