# scripts
a few fun scripts for easy terminal use. 
```bash
cd $HOME && git clone --recurse-submodules git@github.com:zacherywalter/scripts
```
add this to zshrc:
```bash
export PATH=$PATH:~/scripts/bin  # add scripts to path
```

## Commands
```bash
synonym <word>
define <word>
neighbors <word>		# list the 'neighbors' of a word
word_dist <word1> <word2> 	# find the 'hamming distance' between 2 words
big_letters <word>		# write a word in big letters
piy				# python it yourself
```

## Dependencies
expect,
python: enchant		# for installing german dict see word-graph/README.md
