function deductCurrencySimple(amountToDeduct, currentCurrency) {
  const denominations = [
    { name: "gp", value: 1 },
    { name: "sp", value: 0.1 },
    { name: "ep", value: 0.05 },
    { name: "cp", value: 0.01 },
    { name: "pp", value: 10 },
  ];

  let deductableCurrency = 0;
  let convertedChange = 0;

  // Convert the current currency and amount to deduct to the smallest denomination (cp)
  for (denomination of denominations) {
    const name = denomination.name;
    console.log(`deno:${name}`);
    console.log("convertedChange", convertedChange);
    console.log("deductableCurrency", deductableCurrency);
    if (name == "pp" && convertedChange < deductableCurrency) {
      console.log(convertedChange, deductableCurrency);
      continue;
    }
    convertedChange += currentCurrency[name] * denomination.value;
    deductableCurrency += amountToDeduct[name] * denomination.value;
  }

  let remainingCurrency = convertedChange - deductableCurrency;
  let finalCurrency = {};

  // Deduct in the order of gp, sp, ep, cp, and pp
  for (let i = 0; i < denominations.length; i++) {
    const name = denominations[i].name;
    const value = denominations[i].value;
    finalCurrency[name] = Math.floor(remainingCurrency / value);
    remainingCurrency -= finalCurrency[name] * value;
  }

  return finalCurrency;
}

function deductCurrency(currency, amount) {
  const ppValue = 10; // Value of 1 pp in gp
  const gpValue = 1; // Value of 1 gp in gp
  const epValue = 0.5; // Value of 1 ep in gp (1 gp = 2 ep)
  const spValue = 0.1; // Value of 1 sp in gp (1 gp = 10 sp)
  const cpValue = 0.01; // Value of 1 cp in gp (1 gp = 100 cp)

  // Convert the amount to gp for deduction
  const gpAmount =
    amount.pp * ppValue +
    amount.gp +
    amount.ep * epValue +
    amount.sp * spValue +
    amount.cp * cpValue;

  // Check if there is enough currency to deduct
  if (gpAmount >= currency) {
    // Deduct the amount from the input currency
    gpAmount -= currency;

    // Convert back to individual currencies
    const pp = Math.floor(gpAmount / ppValue);
    gpAmount %= ppValue;
    const gp = Math.floor(gpAmount);
    gpAmount %= 1;
    const ep = Math.floor(gpAmount / epValue);
    gpAmount %= epValue;
    const sp = Math.floor(gpAmount / spValue);
    gpAmount %= spValue;
    const cp = Math.round(gpAmount / cpValue);
    console.log({
      pp: pp,
      gp: gp,
      ep: ep,
      sp: sp,
      cp: cp,
    });
    // Return the updated set of objects after deduction
    return {
      pp: pp,
      gp: gp,
      ep: ep,
      sp: sp,
      cp: cp,
    };
  } else {
    // Return null if there is not enough currency to deduct
    return null;
  }
}

//my implementation of the deduct Currency using borrow and reduce method
function borrowAndReduce(currentCurrency, denoIter, denominations) {
  // current denomination
  const currDeno = denominations[denoIter];
  let higherDenoIter = denoIter;
  // until a single denomination's converted coin is higher than the amount deducted, keep running this
  while (higherDenoIter > 0) {
    higherDenoIter--;
    // higher denomination which will be converted to current denomination
    const higherDeno = denominations[higherDenoIter];
    const conversionRate = higherDeno.value / currDeno.value;
    // the amount of higher denomination coins in terms of current denomination
    const borrowableAmount = conversionRate * currentCurrency[higherDeno.name];
    // if higher denomination fulfills the deducted amount
    if (borrowableAmount + currentCurrency[currDeno.name] >= 0) {
      // below three line do:
      // subtracts the amount required to fulfill the requriement
      // converts the remaining higher denominations back into its original denominations
      // subtracts the excess converted denomination from the current denomination which was added in step 1
      const convertedDeno = borrowableAmount + currentCurrency[currDeno.name];
      const remainingHigherDeno = Math.floor(convertedDeno / conversionRate);
      const finalOrigDeno = convertedDeno % conversionRate;
      // console.log(`${finalOrigDeno} ${currDeno.name}`);
      // console.log(`${remainingHigherDeno} ${higherDeno.name}`);
      return {
        ...currentCurrency,
        [currDeno.name]: finalOrigDeno,
        [higherDeno.name]: remainingHigherDeno,
      };
    }
  }
  // if no single denomination is found return null, indicating borrowing not possible
  return null;
}

function deductCurrencyCustom(amountToDeduct, currentCurrency) {
  const denominations = [
    { name: "pp", value: 10 },
    { name: "gp", value: 1 },
    { name: "ep", value: 0.5 },
    { name: "sp", value: 0.1 },
    { name: "cp", value: 0.01 },
  ];

  let updatedCurrency = { ...currentCurrency };

  for (let i = 0; i < denominations.length; i++) {
    const denomination = denominations[i];
    const currDeno = currentCurrency[denomination.name];
    const deductDeno = amountToDeduct[denomination.name];
    if (currDeno >= deductDeno) {
      // console.log("Deduction Possible for:", denomination.name);
      updatedCurrency[denomination.name] = currDeno - deductDeno;
      // console.log(
      //   `${currDeno} - ${deductDeno} = ${updatedCurrency[denomination.name]}`
      // );
    } else {
      console.log("Deduction NOT Possible for:", denomination.name);
      updatedCurrency[denomination.name] = currDeno - deductDeno;
      console.log(
        `${currDeno} - ${deductDeno} != ${
          updatedCurrency[denomination.name]
        } (cannot be negative)`
      );

      const adjustedCurrency = borrowAndReduce(
        updatedCurrency,
        i,
        denominations
      );
      // const higherDeno = denominations[i - 1] ? denominations[i - 1] : null;
      if (adjustedCurrency) {
        updatedCurrency = adjustedCurrency;
      } else {
        console.log(
          `borrowing from a singular higher denomination not possible`
        );
      }
    }
  }
  return updatedCurrency;
}

// Example usage:
const currentCurrency = { pp: 1, gp: 1, ep: 5, sp: 50, cp: 100 }; // Current currency
const amountToDeduct = { pp: 0, gp: 0, ep: 0, sp: 61, cp: 50 }; // Amount to deduct

const updatedCurrency = deductCurrencyCustom(amountToDeduct, currentCurrency);
if (updatedCurrency) {
  console.log("Updated Currency:", updatedCurrency);
} else {
  console.log("Not enough currency to deduct!");
}
