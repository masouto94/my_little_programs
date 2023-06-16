export function isEmpty(value) {
    return (value == null || (typeof value === "string" && value.trim().length === 0));
  }

export function parseDate(toParse) {
  const splitted = toParse.split("-")
  return [parseInt(splitted[0]), parseInt(splitted[1])]
}