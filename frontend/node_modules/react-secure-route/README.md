<h1 align="center">
  react-secure-route
</h1>
<p align="center">
A lightweight secure route components on top of <b><i>react-router-dom</i></b>.
</p>
<p align="center">
It have private, public and protected route, which will give you facility to handle you restricted and authenticated route. These component also gives you route props.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/react-secure-route">
    <img src="https://img.shields.io/npm/v/react-secure-route.svg" alt="Version" />
  </a>
  <a href="https://www.npmjs.com/package/react-secure-route">
    <img src="https://img.shields.io/npm/dw/react-secure-route.svg" alt="Downloads/week" />
  </a>
  <a href="https://github.com/Sawannrl123/react-secure-route/blob/main/package.json">
    <img src="https://img.shields.io/npm/l/react-secure-route.svg" alt="License" />
  </a>
  <a href="https://github.com/Sawannrl123/react-secure-route/network/members">
    <img src="https://img.shields.io/github/forks/Sawannrl123/react-secure-route" alt="Forks on GitHub" />
  </a>
  <a href="https://github.com/Sawannrl123/react-secure-route/stargazers">
    <img src="https://img.shields.io/github/stars/Sawannrl123/react-secure-route" alt="Forks on GitHub" />
  </a>
  <img src="https://badgen.net/bundlephobia/minzip/react-secure-route" alt="minified + gzip size" />
</p>

## Why?

- ![Bundle size](https://badgen.net/bundlephobia/minzip/react-secure-route)
- **No dependencies**
- Light weighted
- Seperate route for public, authenticated and restricated.

## Quick Start

[Demo](https://codesandbox.io/s/react-secure-route-4oqt2)

## Install

```bash
npm install react-secure-route # yarn add react-secure-route
```
#### Usage

```js
import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Link } from "react-router-dom";
import { Home, Login, About } from "./pages";
import { PrivateRoute, ProtectedRoute, PublicRoute } from "react-secure-route";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!localStorage.getItem("isLoggedIn")
  );

  const renderHeader = () => {
    if (isLoggedIn) {
      return (
        <div>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <button
            onClick={() => {
              localStorage.removeItem("isLoggedIn");
              setIsLoggedIn(false);
            }}
          >
            Logout
          </button>
        </div>
      );
    }
    return (
      <div>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <button
          onClick={() => {
            localStorage.setItem("isLoggedIn", true);
            setIsLoggedIn(true);
          }}
        >
          Login
        </button>
      </div>
    );
  };

  return (
    <Router>
      {renderHeader()}
      <Switch>
        <PrivateRoute
          component={Home}
          exact
          isAuthenticated={isLoggedIn}
          redirect="/login"
          path="/"
        />
        <ProtectedRoute
          component={Login}
          restricted={isLoggedIn}
          exact
          redirect="/"
          path="/login"
        />
        <PublicRoute component={About} path="/about" exact />
        /**
         * You can also pass your component like this. You will not get the route props on you component.
          <PrivateRoute
            exact
            isAuthenticated={isLoggedIn}
            redirect="/login"
            path="/"
          >
            <Home />
          </PrivateRoute>
        */
      </Switch>
    </Router>
  );
};

export default App;

```

`Note:- To work this module properly, kindly install react, react-router-dom, and prop-types.`
## `PrivateRoute`

This component handles authentication based on the passed props.

#### Props

| Prop              | Required | Type | Default Value | Description                                                                                                                                                |
| ----------------- | -------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isAuthenticated` | _No_     | bool |     false     | if this is true and restricted props is false your actual component will render else redirect it to passed redirect prop route. | 
| `component` | _No_     | React Component | _ | if component is passed inside component prop, you will get the route props on your component.|
| `children`      | _No_     | React Component | _ | if component is passed as a chidren, you will not get the route props on your component. |   
| `redirect` |  _No_ | string | /login | when authentication fails, it will redirect to the given path with the state from it got redirected. |
| `restricted` |  _No_ | bool | false | if this is true it will redirect to passed redirect prop route. |
| `rest` | _No_ | _ | _ | you can pass the route props of react-router-dom as well. |

## `ProtectedRoute`

This component handles only restricated route based on the passed props.

#### Props

| Prop              | Required | Type | Default Value | Description                                                                                                                                                |
| ----------------- | -------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `component` | _No_     | React Component | _ | if component is passed inside component prop, you will get the route props on your component.|
| `children`      | _No_     | React Component | _ | if component is passed as a chidren, you will not get the route props on your component. |   
| `redirect` |  _No_ | string | / | when authentication fails, it will redirect to the given path with the state from it got redirected. |
| `restricted` |  _No_ | bool | false | if this is true it will redirect to passed redirect prop route. |
| `rest` | _No_ | _ | _ | you can pass the route props of react-router-dom as well. |

## `PublicRoute`

This component is same as `Route` component of `react-router-dom`.

#### Props

| Prop              | Required | Type | Default Value | Description                                                                                                                                                |
| ----------------- | -------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `component` | _No_     | React Component | _ | if component is passed inside component prop, you will get the route props on your component.|
| `children`      | _No_     | React Component | _ | if component is passed as a chidren, you will not get the route props on your component. |   
| `rest` | _No_ | _ | _ | you can pass the route props of react-router-dom as well. |
