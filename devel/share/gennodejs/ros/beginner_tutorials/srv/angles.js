// Auto-generated. Do not edit!

// (in-package beginner_tutorials.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class anglesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.first = null;
      this.second = null;
      this.base = null;
      this.servo1 = null;
      this.servo2 = null;
      this.isSlow = null;
    }
    else {
      if (initObj.hasOwnProperty('first')) {
        this.first = initObj.first
      }
      else {
        this.first = 0;
      }
      if (initObj.hasOwnProperty('second')) {
        this.second = initObj.second
      }
      else {
        this.second = 0;
      }
      if (initObj.hasOwnProperty('base')) {
        this.base = initObj.base
      }
      else {
        this.base = 0;
      }
      if (initObj.hasOwnProperty('servo1')) {
        this.servo1 = initObj.servo1
      }
      else {
        this.servo1 = 0;
      }
      if (initObj.hasOwnProperty('servo2')) {
        this.servo2 = initObj.servo2
      }
      else {
        this.servo2 = 0;
      }
      if (initObj.hasOwnProperty('isSlow')) {
        this.isSlow = initObj.isSlow
      }
      else {
        this.isSlow = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type anglesRequest
    // Serialize message field [first]
    bufferOffset = _serializer.int64(obj.first, buffer, bufferOffset);
    // Serialize message field [second]
    bufferOffset = _serializer.int64(obj.second, buffer, bufferOffset);
    // Serialize message field [base]
    bufferOffset = _serializer.int64(obj.base, buffer, bufferOffset);
    // Serialize message field [servo1]
    bufferOffset = _serializer.int64(obj.servo1, buffer, bufferOffset);
    // Serialize message field [servo2]
    bufferOffset = _serializer.int64(obj.servo2, buffer, bufferOffset);
    // Serialize message field [isSlow]
    bufferOffset = _serializer.bool(obj.isSlow, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type anglesRequest
    let len;
    let data = new anglesRequest(null);
    // Deserialize message field [first]
    data.first = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [second]
    data.second = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [base]
    data.base = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [servo1]
    data.servo1 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [servo2]
    data.servo2 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [isSlow]
    data.isSlow = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 41;
  }

  static datatype() {
    // Returns string type for a service object
    return 'beginner_tutorials/anglesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9cb918e313d93f1f1b66c65d5100a33d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 first
    int64 second
    int64 base
    int64 servo1
    int64 servo2
    bool isSlow
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new anglesRequest(null);
    if (msg.first !== undefined) {
      resolved.first = msg.first;
    }
    else {
      resolved.first = 0
    }

    if (msg.second !== undefined) {
      resolved.second = msg.second;
    }
    else {
      resolved.second = 0
    }

    if (msg.base !== undefined) {
      resolved.base = msg.base;
    }
    else {
      resolved.base = 0
    }

    if (msg.servo1 !== undefined) {
      resolved.servo1 = msg.servo1;
    }
    else {
      resolved.servo1 = 0
    }

    if (msg.servo2 !== undefined) {
      resolved.servo2 = msg.servo2;
    }
    else {
      resolved.servo2 = 0
    }

    if (msg.isSlow !== undefined) {
      resolved.isSlow = msg.isSlow;
    }
    else {
      resolved.isSlow = false
    }

    return resolved;
    }
};

class anglesResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.check = null;
    }
    else {
      if (initObj.hasOwnProperty('check')) {
        this.check = initObj.check
      }
      else {
        this.check = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type anglesResponse
    // Serialize message field [check]
    bufferOffset = _serializer.bool(obj.check, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type anglesResponse
    let len;
    let data = new anglesResponse(null);
    // Deserialize message field [check]
    data.check = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'beginner_tutorials/anglesResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c5df00fea9d1f39520fa0345cbde1b26';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool check
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new anglesResponse(null);
    if (msg.check !== undefined) {
      resolved.check = msg.check;
    }
    else {
      resolved.check = false
    }

    return resolved;
    }
};

module.exports = {
  Request: anglesRequest,
  Response: anglesResponse,
  md5sum() { return 'd61f65b1d41fa5ce5b8822fbdbff89c7'; },
  datatype() { return 'beginner_tutorials/angles'; }
};
