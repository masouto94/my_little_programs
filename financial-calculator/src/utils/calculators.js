function dateDiffInDays(from, to) {
    const fromAsDate = new Date(from)
    const toAsDate = new Date(to)
    const _MS_PER_DAY = 1000 * 60 * 60 * 24;
    // Discard the time and time-zone information.
    const utc1 = Date.UTC(fromAsDate.getFullYear(), fromAsDate.getMonth(), fromAsDate.getDate());
    const utc2 = Date.UTC(toAsDate.getFullYear(), toAsDate.getMonth(), toAsDate.getDate());
    return Math.floor((utc2 - utc1) / _MS_PER_DAY);
  }
  

export const calculateCompuondInterest = (amount, interest, from,to) => {
    if(from === to){
        return amount
    }
    const diffInDays = dateDiffInDays(from,to)
    const dailyInterest = (interest / 30).toFixed(4)
    let initial = true
    for (let i = 0; i < diffInDays; i++) {
        if(initial){
            initial=false
            i++
            continue
        }
        amount *=  (1 + dailyInterest / 100 ).toFixed(4)
    }
    return amount.toFixed(4)
}