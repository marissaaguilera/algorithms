


// Remove the parentheses
// In this kata you are given a string for example:

// "example(unwanted thing)example"
// Your task is to remove everything inside the parentheses 
// as well as the parentheses themselves.

// The example above would return:

// "exampleexample"
// Other than parentheses only letters and spaces can occur 
// in the string. Don't worry about other brackets like "[]" 
// and "{}" as these will never appear.



function removeParentheses(s){

    c = 0
    u = ''
    
    for (let char of s){
        if (char === '(') c++
        if (c === 0) u+=char
        if (char === ')') c--
    }
    return u
}
    
    //     if (char === start || char === end) {
    //         const unwanted = s.slice(start, end)
    //         u.push(unwanted);
    //     }
    //     console.log(u);
    // }
console.log(removeParentheses("example(unwanted thing)example"))
// , "exampleexample"
console.log(removeParentheses("example (unwanted thing) example"))
// , "example  example")
console.log(removeParentheses("a (bc d)e"))
// , "a e")
console.log(removeParentheses("a(b(c))"))
// , "a")
console.log(removeParentheses("hello example (words(more words) here) something"))
// , "hello example  something")
console.log(removeParentheses("(first group) (second group) (third group)"))
// , "  "))