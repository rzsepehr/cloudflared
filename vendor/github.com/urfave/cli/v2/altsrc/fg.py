# Only types that provide implementation of FlagInputSourceExtension can be listed here
# please keep list sorted alphabetically
flag_types = [
    "Bool",
    "Duration",
    "Float64",
    "Generic",
    "Int",
    "IntSlice",
    "Path",
    "String",
    "StringSlice",
]

print('''// Code generated by fg.py; DO NOT EDIT.

package altsrc

import (
	"flag"

	"github.com/urfave/cli/v2"
)''')

for t in flag_types:
    print(f'''
// {t}Flag is the flag type that wraps cli.{t}Flag to allow
// for other values to be specified
type {t}Flag struct {{
	*cli.{t}Flag
	set *flag.FlagSet
}}
var _ FlagInputSourceExtension = (*{t}Flag)(nil)

// New{t}Flag creates a new {t}Flag
func New{t}Flag(fl *cli.{t}Flag) *{t}Flag {{
	return &{t}Flag{{{t}Flag: fl, set: nil}}
}}

// Apply saves the flagSet for later usage calls, then calls
// the wrapped {t}Flag.Apply
func (f *{t}Flag) Apply(set *flag.FlagSet) error {{
	f.set = set
	return f.{t}Flag.Apply(set)
}}''')