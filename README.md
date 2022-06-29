# RS-Web-Dev

# Class 1 (HTML)
## What is HTML 

`HTML codes tells the browser how to structure the Web page`

![html1](https://i.ibb.co/t3QpLSR/html1.jpg)

### Document Tree

![Logo](https://i.ibb.co/0DtX0Gh/html2.png)

`Tree of HTML Elements`

```<tagname>Content</tagname>```

```<tagname />```

## Installation and Code editor

`https://www.sublimetext.com/download`

`https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello`

## HTML Elements

### HTML boilerplate

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <title>RS Class 1</title>
  </head>
  <body>
    <!-- Content Goes here -->
  </body>
</html>

```

### Header tags

```html
<h1>I am h1</h1>
<h2>I am h2</h2>
<h3>I am h3</h3>
<h4>I am h4</h4>
<h5>I am h5</h5>
<h6>I am h6</h6>
```
![Logo](https://i.ibb.co/QYsxpBP/html4.jpg)

### Paragraph

```html
<p>I am a paragraph</p>
```

### Break and Horizontal rule tag

```html
<br />
```

![Logo](https://i.ibb.co/SdgyfMd/html3.jpg)

```html
<hr />
```

### Text formatting tag

```html
<strong>I am Strong 💪</strong>
<small>I am smol 😔</small>
<mark>mark me</mark>
<del>please, do not write off me :(</del>
```

### Division tag

```html
<div>I am divided</div>
```

### List

`Types of list`

- Orderd list

```html
<ul>
    <li>Like</li>
    <li>Comment</li>
    <li>Subscribe</li>
</ul>
```

- Unorderd list

```html
<ol>
    <li>Get Admitted to BracU</li>
    <li>Enroll in Tarc</li>
    <li>Find Jiboner mane 💑</li>
</ol>
```

- Definition list

```html
<dl>
    <dt>Get Admitted to BracU</dt>
    <dd>Ektu pera</dd>
    <dt>Enroll in Tarc</dt>
    <dd>Now ektu happy</dd>
    <dt>Find Jiboner mane 💑</dt>
    <dd>Now pura happy</dd>
</dl>
```

### Image Tag

```html
<img src="images/html1.jpg" width="200" height="200" alt="dp" />
```

### Anchor tag

```html
<a href="https://www.youtube.com/">Youtube</a>
<a href="https://www.youtube.com/"
target="_blank">Youtube</a>
```

### Table tag

```html
<table>
  <thead>
    <tr>
      <th>Heading 1</th>
      <th>Heading 2</th>
      <th>Heading 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I am 1</td>
      <td>I am 2</td>
      <td>I am 3</td>
    </tr>
    <tr>
      <td>I am 2.1</td>
      <td>I am 2.2</td>
      <td>I am 2.3</td>
    </tr>
  </tbody>
</table>
```

### Form 

```html
<form>
  <label>Enter Username</label><br />
  <input type="text" /><hr />

  <label>Enter Email</label><br />
  <input type="email" /><hr />

  <label>Enter Password</label><br />
  <input type="password" /><hr />
</form>
```

### Details tag

```html
<details>
  <summary>Please Open</summary>
  <p>haha I got you</p>
</details>
```

### Input

```html
  <input type="text" /><br />

  <input type="email" /><br />

  <input type="password" /><br />

  <input type="color" /><br />

  <input type="time" /><br />
  
  <input type="month" /><br />
  
  <input type="file" /><br />

```

### Form 

```html
  <form>
    <label>Enter Username</label><br />
    <input type="text" /><br />

    <label>Enter Email</label><br />
    <input type="email" /><br />

    <label>Enter Password</label><br />
    <input type="password" /><br />

    <label>Tell me about yourself</label><br />
    <textarea ></textarea ><br />

    <label>Enter Profile Picture</label><br />
    <input type="file" /><br />

    <label>Select semester</label>
    <select>
      <option value="1st">1st Semester</option>
      <option value="2nd">2nd Semester</option>
      <option value="3rd">3rd Semester</option>
    </select>

    <button>Submit</button>
  </form>
```

### HTML Sementic Tags

![Logo](https://www.w3schools.com/html/img_sem_elements.gif)

[For more](https://www.w3schools.com/html/html5_semantic_elements.asp)

### Ending

![meme](https://i.imgflip.com/u9pv5.jpg)



# Class 2 (CSS 1.0)

` CSS or Cascading Style Sheet is used to style HTML Document `

![Logo](https://images-cdn.9gag.com/photo/amz44B4_700b.jpg)


## Styling Structure

```css
selector {
  style declaration (Key (property) - Value (value))
}
```

` Selectors `
  - universal
  - element 
  - class
  - id 


## Implementing on HTML

  - Inline Styling
  - Internal Style Sheet
  - External Style Sheet

### Inline Styling

```html
<p style="color: red" >I am Red</p>
```

### Internal Style Sheet

```html
</head>

<style>
  p {
    color: red
  }
</style>

<body>
```

### External Style Sheet

` Create a file name style.css (can be anyname).css ` 

```html
<link rel="stylesheet" href="style.css" >
```

### Universal Selector

```css
* {
  color: red
}
```

### Element Selector

```css
p {
  color: red
}
```

### Class Selector

```css
.red {
  color: red
}
```

```html
<h1 Class="red">I am Red</h1>
<p Class="red">I am Red</p>
```

### Id Selector

```css
#red {
  color: red
}
```

```html
<h1 id="red">I am Green</h1>
```


## Styling declaration we must know

### Color 
  - ` font color (color: red) `
  - ` Background color (background-color: red) `

  ` Using Color `
  - color name (ex. red)
  - Hex value of color (ex. #121212)
  - RGBA (ex. rgba(0, 5, 6, 1))


### Font 
  - ` Font Style (font-family: sans-serif) `
  - ` Font weight (font-weight: lighter/bold/(100-900)) `
  - ` Font size (font-size: large/small/medium/px) `

  ` https://fonts.google.com/ `


### Text 
  - ` Text Position (text-align: center/left/right) `
  - ` Distance between Letter (letter-spacing: 10px;) `
  - ` Distance between Words (word-spacing: 10px;) `
  - ` Distance between Lines (line-height: 60px;) `


### List 
  - ` List Style (list-style: disc/square/circle/none) `


## Display

- Block (Takes the whole width ex. div, h1, p)
- Inline (Takes as mush as needed ex. span)

```css
  display: inline/block/none
```  

### Table 

```css
th, td {
    border: 1px solid blue;
    font-size: 60px;
    height: 100px;
}

th {
    background-color: aquamarine;
}

table {
    border-collapse: collapse;
    text-align: center;
    vertical-align: middle;
    width: 70%;
}
```


## CSS Box Model

![Logo](https://media.gcflearnfree.org/content/5ef2084faaf0ac46dc9c10be_06_23_2020/box_model.png)


![Logo](https://www.messenger.com/messenger_media/?thread_id=100028718222452&attachment_id=1429462294185746&message_id=mid.%24cAAAADX0GUBCH4EqWwGBrwVEplIM4)

### Demo
```css
.box {
    border: 1px solid blue; (left/top/bottom/right)
    border-radius: 10px;
    padding: 10px; (left/top/bottom/right)
    margin: 10px; (left/top/bottom/right)
}
```

## Spcificity

` element < class < id < inline styling < !important `


## Hover 

```css
selector:hover {
    style declaration
}
```


# Class 3 (CSS 2.0)

## Flex Box
`The Flexible Box Layout Module, makes it easier to design flexible responsive layout structure`

### Demo 

```css
.boxes {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
}

.boxes div {
    background-color: aqua;
    border: 1px solid black;
    height: 250px;
    width: 250px;
    margin: 5px;
}

.box-1{
    flex: 2;
}
.box-2{
    flex: 1;
}
.box-3{
    flex: 1;
}
```