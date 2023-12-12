// Auto-generated. Do not edit!

// (in-package beginner_tutorials.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class anglesMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.first = null;
      this.second = null;
      this.base = null;
      this.servo1 = null;
      this.servo2 = null;
      this.isPump = null;
    }
    else {
      if (initObj.hasOwnProperty('first')) {
        this.first = initObj.first
      }
      else {
        this.first = 0.0;
      }
      if (initObj.hasOwnProperty('second')) {
        this.second = initObj.second
      }
      else {
        this.second = 0.0;
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
      if (initObj.hasOwnProperty('isPump')) {
        this.isPump = initObj.isPump
      }
      else {
        this.isPump = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type anglesMsg
    // Serialize message field [first]
    bufferOffset = _serializer.float64(obj.first, buffer, bufferOffset);
    // Serialize message field [second]
    bufferOffset = _serializer.float64(obj.second, buffer, bufferOffset);
    // Serialize message field [base]
    bufferOffset = _serializer.char(obj.base, buffer, bufferOffset);
    // Serialize message field [servo1]
    bufferOffset = _serializer.int64(obj.servo1, buffer, bufferOffset);
    // Serialize message field [servo2]
    bufferOffset = _serializer.int64(obj.servo2, buffer, bufferOffset);
    // Serialize message field [isPump]
    bufferOffset = _serializer.bool(obj.isPump, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type anglesMsg
    let len;
    let data = new anglesMsg(null);
    // Deserialize message field [first]
    data.first = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [second]
    data.second = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [base]
    data.base = _deserializer.char(buffer, bufferOffset);
    // Deserialize message field [servo1]
    data.servo1 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [servo2]
    data.servo2 = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [isPump]
    data.isPump = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 34;
  }

  static datatype() {
    // Returns string type for a message object
    return 'beginner_tutorials/anglesMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '926bd9e23b51251f5bd37bbd4418b9f6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 first
    float64 second
    char base
    int64 servo1 
    int64 servo2
    bool isPump
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new anglesMsg(null);
    if (msg.first !== undefined) {
      resolved.first = msg.first;
    }
    else {
      resolved.first = 0.0
    }

    if (msg.second !== undefined) {
      resolved.second = msg.second;
    }
    else {
      resolved.second = 0.0
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

    if (msg.isPump !== undefined) {
      resolved.isPump = msg.isPump;
    }
    else {
      resolved.isPump = false
    }

    return resolved;
    }
};

module.exports = anglesMsg;
