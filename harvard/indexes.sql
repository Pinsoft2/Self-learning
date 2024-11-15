CREATE INDEX "course_index" ON "courses"("id","title","semester");

CREATE INDEX "student_index" ON "students"("id");

CREATE INDEX "enrollment_index" ON "enrollments"("course_id");