;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::anglesMsg)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'anglesMsg (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ANGLESMSG")
  (make-package "BEGINNER_TUTORIALS::ANGLESMSG"))

(in-package "ROS")
;;//! \htmlinclude anglesMsg.msg.html


(defclass beginner_tutorials::anglesMsg
  :super ros::object
  :slots (_first _second _base _servo1 _servo2 _servo3 _isPump ))

(defmethod beginner_tutorials::anglesMsg
  (:init
   (&key
    ((:first __first) 0.0)
    ((:second __second) 0.0)
    ((:base __base) 0.0)
    ((:servo1 __servo1) 0)
    ((:servo2 __servo2) 0)
    ((:servo3 __servo3) 0)
    ((:isPump __isPump) nil)
    )
   (send-super :init)
   (setq _first (float __first))
   (setq _second (float __second))
   (setq _base (float __base))
   (setq _servo1 (round __servo1))
   (setq _servo2 (round __servo2))
   (setq _servo3 (round __servo3))
   (setq _isPump __isPump)
   self)
  (:first
   (&optional __first)
   (if __first (setq _first __first)) _first)
  (:second
   (&optional __second)
   (if __second (setq _second __second)) _second)
  (:base
   (&optional __base)
   (if __base (setq _base __base)) _base)
  (:servo1
   (&optional __servo1)
   (if __servo1 (setq _servo1 __servo1)) _servo1)
  (:servo2
   (&optional __servo2)
   (if __servo2 (setq _servo2 __servo2)) _servo2)
  (:servo3
   (&optional __servo3)
   (if __servo3 (setq _servo3 __servo3)) _servo3)
  (:isPump
   (&optional (__isPump :null))
   (if (not (eq __isPump :null)) (setq _isPump __isPump)) _isPump)
  (:serialization-length
   ()
   (+
    ;; float64 _first
    8
    ;; float64 _second
    8
    ;; float64 _base
    8
    ;; int64 _servo1
    8
    ;; int64 _servo2
    8
    ;; int64 _servo3
    8
    ;; bool _isPump
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _first
       (sys::poke _first (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _second
       (sys::poke _second (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _base
       (sys::poke _base (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _servo1
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _servo1 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _servo1) (= (length (_servo1 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_servo1 . bv) 0) 0) s)
              (write-long (ash (elt (_servo1 . bv) 1) -1) s))
             ((and (class _servo1) (= (length (_servo1 . bv)) 1)) ;; big1
              (write-long (elt (_servo1 . bv) 0) s)
              (write-long (if (>= _servo1 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _servo1 s)(write-long (if (>= _servo1 0) 0 #xffffffff) s)))
     ;; int64 _servo2
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _servo2 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _servo2) (= (length (_servo2 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_servo2 . bv) 0) 0) s)
              (write-long (ash (elt (_servo2 . bv) 1) -1) s))
             ((and (class _servo2) (= (length (_servo2 . bv)) 1)) ;; big1
              (write-long (elt (_servo2 . bv) 0) s)
              (write-long (if (>= _servo2 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _servo2 s)(write-long (if (>= _servo2 0) 0 #xffffffff) s)))
     ;; int64 _servo3
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _servo3 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _servo3) (= (length (_servo3 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_servo3 . bv) 0) 0) s)
              (write-long (ash (elt (_servo3 . bv) 1) -1) s))
             ((and (class _servo3) (= (length (_servo3 . bv)) 1)) ;; big1
              (write-long (elt (_servo3 . bv) 0) s)
              (write-long (if (>= _servo3 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _servo3 s)(write-long (if (>= _servo3 0) 0 #xffffffff) s)))
     ;; bool _isPump
       (if _isPump (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _first
     (setq _first (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _second
     (setq _second (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _base
     (setq _base (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _servo1
#+(or :alpha :irix6 :x86_64)
      (setf _servo1 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _servo1 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _servo2
#+(or :alpha :irix6 :x86_64)
      (setf _servo2 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _servo2 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _servo3
#+(or :alpha :irix6 :x86_64)
      (setf _servo3 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _servo3 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; bool _isPump
     (setq _isPump (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get beginner_tutorials::anglesMsg :md5sum-) "6b8e0d4ccdce3065f67c69afb3a3bac4")
(setf (get beginner_tutorials::anglesMsg :datatype-) "beginner_tutorials/anglesMsg")
(setf (get beginner_tutorials::anglesMsg :definition-)
      "float64 first
float64 second
float64 base
int64 servo1 
int64 servo2
int64 servo3
bool isPump
")



(provide :beginner_tutorials/anglesMsg "6b8e0d4ccdce3065f67c69afb3a3bac4")


