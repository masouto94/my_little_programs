// function dateDiffInDays(from, to) {
//     const fromAsDate = new Date(from)
//     const toAsDate = new Date(to)
//     const _MS_PER_DAY = 1000 * 60 * 60 * 24;
//     // Discard the time and time-zone information.
//     const utc1 = Date.UTC(fromAsDate.getFullYear(), fromAsDate.getMonth(), fromAsDate.getDate());
//     const utc2 = Date.UTC(toAsDate.getFullYear(), toAsDate.getMonth(), toAsDate.getDate());
//     return Math.floor((utc2 - utc1) / _MS_PER_DAY);
//   }
  

export const calculateCompoundInterest = (amount, interest, interval, repetitions) => {
    let dailyInterest = (interest / 365 * interval)
    for (let i = 1; i <= repetitions; i++) {

        amount *=  (1 + dailyInterest / 100 )
    }
    return amount.toFixed(4)
}