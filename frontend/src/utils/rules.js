/* eslint-disable */

const urlRegex = /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/
const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
const hexRegex = /^[0-9A-F]+$/
const alphaNumericRegex = /^[a-z0-9]+$/i
const alphaNumericWithDotRegex = /^[a-z\d\.\s]+$/i
const alphaNumericWithDotAndPoundRegex = /^[a-z\d\.&'()\#\s]+$/i

export default {
  notEmpty: v => !!v && v.trim().length > 0 || 'Field cannot be empty',
  maxSize: size =>  (value => !value || value.size < size || `Image size should be less than ${size/1000} KB!`),
  isRequired: v => !!v || 'Field cannot be empty',
  maxSize: size =>  (value => !value || value.size < size || `Image size should be less than ${size/1000} KB!`),
  isEmail: v => emailRegex.test(v) || 'Invalid Email',
  isEmailWithEmpty: v => (!v || emailRegex.test(v) || 'Invalid Email'),
  minCharacters: count => (v => !!v && v.length >= count || 
  `Must be at least ${count} characters`),
  maxCharacters: count => (v => !!v && v.length <= count || 
    `Max ${count} characters are allowed`),
  exactCharacters: count => (v => !!v && v.length === count || 
  `Must be exactly ${count} characters`),
  isNumeric: v => /^[0-9]+$/.test(v) || 'Must be numbers only',
  isNumericAndNegative: v => /^-?[0-9]+$/.test(v) || 'Must be numbers only',
  isInteger: v => !isNaN(parseInt(v)) || 'Must be an integer only',
  isFloat: v => !isNaN(parseFloat(v)) || 'Must be a decimal number',
  isNonZero: v => (!isNaN(parseInt(v)) && parseInt(v) > 0) || 'Must be a number > 0',
  isPositive: v => (!isNaN(parseInt(v)) && parseInt(v) >= 0) || 'Must be a number >= 0',
  isInfinityOrPositive: v => (v == window.Infinity || !isNaN(parseInt(v)) && parseInt(v) > 0) || 'Must be a number > 0',
  isHour: v => /^[0-2]\d\:[0-2]\d\:[0-5]\d$/.test(v) || 'Must be in HH:MM:SS format',
  isHourMinutes: v => /^[0-2]\d\:[0-2]\d\$/.test(v) || 'Must be in HH:MM format',
  isURL: v => urlRegex.test(v) || 'Invalid URL',
  isRank: v => !isNaN(parseInt(v)) && parseInt(v) >= 1 || 'Must be an integer > 1',
  maxNumber: max => (v => !isNaN(parseFloat(v)) && parseFloat(v)<= max ||
  `Must be maximum ${max}`),
  minNumber: min => (v => !isNaN(parseFloat(v)) && parseFloat(v)>= min ||
  `Must be minimum ${min}`),
  isHex: v => hexRegex.test(v) || 'Must be a hexadecimal string',
  alphaNumeric : v => alphaNumericRegex.test(v) || 'Must be alphanumeric',
  alphaNumericWithDot: v => alphaNumericWithDotRegex.test(v) || 'Must be alphanumeric',
  alphaNumericWithDotWithPound: v => alphaNumericWithDotAndPoundRegex.test(v) || 'Must be alphanumeric',
  shouldBeMinValue: (v, min ) => {return v >= min || `Must be greater than ${min} `}
}