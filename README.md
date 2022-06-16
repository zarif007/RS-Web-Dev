# RS-Web-Dev

# Class 1
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
<a href="https://www.youtube.com/watch?v=N8YMl4Ezp4g">Youtube</a>
<a href="https://www.youtube.com/watch?v=N8YMl4Ezp4g"
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
