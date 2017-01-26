// ES5
'use strict';

function User(name){
  this._name = name;
}

User.prototype = Object.create(null, {
  constructor: {
    value: User
  },

  say: {
    value: function() {
      return 'My name is ' + this._name;
    }
  }
});

function Admin(name) {
  User.apply(this, arguments);
}

Admin.prototype = Object.create(User.prototype, {
  constructor: {
    value: Admin
  },

  say: {
    value: function() {
      var superClassPrototype =  Object.getPrototypeOf(this.constructor.prototype);
      return '[Administrator] ' + superClassPrototype.say.call(this);
    }
  }
});

var user = new User('Alice');
console.log(user.say()); // My name is Alice

var admin = new Admin('Bob');
console.log(admin.say()); // [Administrator] My name is Bob
