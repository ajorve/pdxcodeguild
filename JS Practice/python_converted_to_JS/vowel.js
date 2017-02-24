/**
 * Created by Anders on 2/20/2017.
 */


var letter_input = prompt("Please enter a letter. >> ");

var vowels = ['a', 'e', 'i', 'o', 'u'];

if (vowels.indexOf(letter_input) !== -1) {
        alert('This is a vowel!');
    } else {
        alert('This is NOT a vowel!');
    }
}