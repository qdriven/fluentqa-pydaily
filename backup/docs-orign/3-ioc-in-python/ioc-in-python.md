# IoC in Python

> At its heart, Injector is simply a dictionary for
  mapping types to things that create instances of 
  those types. This could be as simple as:
  ```{str: 'an instance of a string'}```

There are a lot of instances stored in a key-value manner.

## Concepts

- ClassProvider: create new instance from class
- InstanceProvider: return exiting instance
- CallableProvider: provide an instance by calling a function
- Scope:
  - Singleton Scope
  - Threading Scope or Request Scope
  - No-Scope as default
- Binder:
  - Create Key-Value Relation as binding
- Module:
  - config binding
- injection:
  - providing an instance of a type to a method