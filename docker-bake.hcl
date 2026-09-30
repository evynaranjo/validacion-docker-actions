group "default" {
  targets = ["app"]
}

target "app" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["validacion-docker:latest"]
}
