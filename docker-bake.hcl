group "default" {
  targets = ["web", "celery"]
}

target "web" {
  context = "."
  dockerfile = "Dockerfile"
  tags = ["vendor_web_app:latest"]
}

target "celery" {
  context = "."
  dockerfile = "Dockerfile"
  tags = ["celery_worker:latest"]
}
