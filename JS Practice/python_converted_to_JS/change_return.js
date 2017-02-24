"use strict";


function ChangeReturn(UserChange) {
    var rem = Math.floor(UserChange);
    var dollars = Math.floor(rem / 100);
    rem = rem - (dollars * 100);
    var quarters = Math.floor(rem / 25);
    rem = rem - (quarters * 25);
    var dimes = Math.floor(rem / 10);
    rem = rem - (dimes * 10);
    var nickles = Math.floor(rem / 5);
    rem = rem - (nickles * 5);
    var pennies = rem;

    document.write('Dollars: ' + dollars + '<br>' + 'Quarters: ' + quarters + '<br>' + 'Dimes: ' + dimes + '<br>' + 'Nickles: ' + nickles + '<br>' + 'Pennies: ' + pennies);
    alert('Dollars: ' + dollars + '\n' + 'Quarters: ' + quarters + '\n' + 'Dimes: ' + dimes + '\n' + 'Nickles: ' + nickles + '\n' + 'Pennies: ' + pennies);
}
const UserChange = prompt("How much change do you want dispensed? >> ");

ChangeReturn(UserChange);