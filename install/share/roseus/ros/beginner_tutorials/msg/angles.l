;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::angles)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'angles (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ANGLES")
  (make-package "BEGINNER_TUTORIALS::ANGLES"))

(in-package "ROS")
;;//! \htmlinclude angles.msg.html


(defclass beginner_tutorials::angles
  :super ros::object
  :slots (_first _second _base ))

(defmethod beginner_tutorials::angles
  (:init
   (&key
    ((:first __first) 0)
    ((:second __second) 0)
    ((:base __base) 0)
    )
   (send-super :init)
   (setq _first (round __first))
   (setq _second (round __second))
   (setq _base (round __base))
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
  (:serialization-length
   ()
   (+
    ;; int64 _first
    8
    ;; int64 _second
    8
    ;; int64 _base
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _first
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _first (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _first) (= (length (_first . bv)) 2)) ;; bignum
              (write-long (ash (elt (_first . bv) 0) 0) s)
              (write-long (ash (elt (_first . bv) 1) -1) s))
             ((and (class _first) (= (length (_first . bv)) 1)) ;; big1
              (write-long (elt (_first . bv) 0) s)
              (write-long (if (>= _first 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _first s)(write-long (if (>= _first 0) 0 #xffffffff) s)))
     ;; int64 _second
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _second (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _second) (= (length (_second . bv)) 2)) ;; bignum
              (write-long (ash (elt (_second . bv) 0) 0) s)
              (write-long (ash (elt (_second . bv) 1) -1) s))
             ((and (class _second) (= (length (_second . bv)) 1)) ;; big1
              (write-long (elt (_second . bv) 0) s)
              (write-long (if (>= _second 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _second s)(write-long (if (>= _second 0) 0 #xffffffff) s)))
     ;; int64 _base
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _base (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _base) (= (length (_base . bv)) 2)) ;; bignum
              (write-long (ash (elt (_base . bv) 0) 0) s)
              (write-long (ash (elt (_base . bv) 1) -1) s))
             ((and (class _base) (= (length (_base . bv)) 1)) ;; big1
              (write-long (elt (_base . bv) 0) s)
              (write-long (if (>= _base 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _base s)(write-long (if (>= _base 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _first
#+(or :alpha :irix6 :x86_64)
      (setf _first (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _first (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _second
#+(or :alpha :irix6 :x86_64)
      (setf _second (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _second (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _base
#+(or :alpha :irix6 :x86_64)
      (setf _base (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _base (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get beginner_tutorials::angles :md5sum-) "0496e8c0c35c632938a659f27c1ce0a3")
(setf (get beginner_tutorials::angles :datatype-) "beginner_tutorials/angles")
(setf (get beginner_tutorials::angles :definition-)
      "int64 first
int64 second
int64 base
")



(provide :beginner_tutorials/angles "0496e8c0c35c632938a659f27c1ce0a3")


