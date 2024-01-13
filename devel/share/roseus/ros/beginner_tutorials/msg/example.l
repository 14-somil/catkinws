;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::example)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'example (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::EXAMPLE")
  (make-package "BEGINNER_TUTORIALS::EXAMPLE"))

(in-package "ROS")
;;//! \htmlinclude example.msg.html


(defclass beginner_tutorials::example
  :super ros::object
  :slots (_data ))

(defmethod beginner_tutorials::example
  (:init
   (&key
    ((:data __data) 0.0)
    )
   (send-super :init)
   (setq _data (float __data))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; float64 _data
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _data
       (sys::poke _data (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _data
     (setq _data (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get beginner_tutorials::example :md5sum-) "fdb28210bfa9d7c91146260178d9a584")
(setf (get beginner_tutorials::example :datatype-) "beginner_tutorials/example")
(setf (get beginner_tutorials::example :definition-)
      "float64 data
")



(provide :beginner_tutorials/example "fdb28210bfa9d7c91146260178d9a584")


