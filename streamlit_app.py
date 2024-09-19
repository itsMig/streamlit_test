import streamlit as st 

'Hello world'


_ = """
# Header

Hello World!

- one
- two
- three


[HI](www.test.de)


*italic*

**bold**

***boldITa***


|  col1 | col2|
|------:|:----|
  | 1 | 5 |


-[x] retz
-[ ] not



The background color is `#ffffff` for light mode and `#000000` for dark mode.

`code`
HEX	`#RRGGBB`	`#0969DA`	Screenshot of rendered GitHub Markdown showing how HEX value #0969DA appears with a blue circle.
RGB	`rgb(R,G,B)`	`rgb(9, 105, 218)`	Screenshot of rendered GitHub Markdown showing how RGB value 9, 105, 218 appears with a blue circle.
HSL	`hsl(H,S,L)`	`hsl(212, 92%, 45%)`	Screenshot of rendered GitHub Markdown showing how HSL value 212, 92%, 45% appears with a blue circle.

```python
if __name__ == '__main__':
    run()
```



## ghtreds
Sentence1 .......
Sentence 2......

ew block

~~stirkethrough~~

sadfghjgfds<sup>stirkethrough</sup>
"""


st.write(_)
