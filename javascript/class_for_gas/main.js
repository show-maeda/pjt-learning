function main() {
  var
    satoshi = new Human('satoshi', 160, 75),
    masami = new Human('masami', 152, 54)
  ;

  satoshi.sayHello()
  masami.sayHello()

  Logger.log('---')

  masami.sayBMI()
  masami.changeWeight(-3)
  masami.setBMI()
  masami.sayBMI()

  Logger.log('---')

  satoshi.sayBMI()
}
