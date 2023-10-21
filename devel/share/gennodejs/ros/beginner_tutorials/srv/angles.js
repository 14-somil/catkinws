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
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'beginner_tutorials/anglesRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0496e8c0c35c632938a659f27c1ce0a3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 first
    int64 second
    int64 base
    
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
  md5sum() { return '644940150eafdcd9dda035c968198107'; },
  datatype() { return 'beginner_tutorials/angles'; }
};
