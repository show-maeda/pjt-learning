var Human = function(name, height, weight) {
  this.name = name;
  this.height = height;
  this.weight = weight;

};

Human.prototype.sayHello = function() {
  Logger.log("Hello I'm " + this.name);
};

// BMIをセット
Human.prototype.setBMI = function() {
  Logger.log('setBMI')
  m_height = this.height/100;
  bmi = this.weight / (m_height * m_height)
  this.bmi = bmi;
};

// BMIを叫ぶ
Human.prototype.sayBMI = function() {
  Logger.log('sayBMI')
  if (this.bmi) {
    Logger.log('My BMI score is ' + this.bmi);
  } else {
    this.setBMI();
    Logger.log('My BMI score is ' + this.bmi);
  }
};

// 体重を変える
Human.prototype.changeWeight = function(diff) {
  this.weight = this.weight + diff;
}