---
outline: deep
---

# Request and response shapes

This page describes the JSON shapes used by the Dployr HTTP API. The Python and
TypeScript SDKs map directly to these objects.

---

## Common types

### Runtime

Identifies the runtime for a service or deployment.

```jsonc
"static" | "golang" | "php" | "python" | "nodejs" | "ruby" | "dotnet" | "java" | "docker" | "k3s" | "custom"
```

### RuntimeObj

```jsonc
{
  "type": "nodejs",      // one of Runtime
  "version": "18.0.0"    // optional
}
```

### RemoteObj

```jsonc
{
  "url": "https://github.com/user/repo.git",
  "branch": "main",
  "commit_hash": "abc123def456"
}
```

---

## Deployments

### DeployRequest (POST /deployments)

```jsonc
{
  "name": "my-app",                 // required
  "description": "My app",          // optional
  "user_id": "user-123",           // required
  "source": "remote",              // required: "remote" | "image"
  "runtime": {                       // required
    "type": "nodejs",
    "version": "18.0.0"
  },
  "version": "v1.0.0",             // optional
  "run_cmd": "npm start",          // optional
  "build_cmd": "npm run build",    // optional
  "port": 3000,                      // optional (1–65535)
  "working_dir": "/app",           // optional
  "static_dir": "/app/dist",       // optional
  "image": "node:18-alpine",       // used when source == "image"
  "env_vars": {                      // optional
    "NODE_ENV": "production"
  },
  "secrets": {                       // optional
    "MY_SECRET": "value"
  },
  "remote": {                        // optional, used when source == "remote"
    "url": "https://github.com/user/repo.git",
    "branch": "main",
    "commit_hash": "abc123def456"
  },
  "domain": "myapp.example.com",   // optional
  "dns_provider": "cloudflare"     // optional
}
```

### DeployResponse

```jsonc
{
  "success": true,
  "id": "01HN2K3M4N5P6Q7R8S9T0U1V2W",
  "name": "my-app",
  "created_at": "2024-01-01T12:00:00Z"
}
```

### Deployment (elements of deployments list)

```jsonc
{
  "id": "01HN2K3M4N5P6Q7R8S9T0U1V2W",
  "user_id": "user-123",
  "user_email": "user@example.com",
  "config": { /* Blueprint, see below */ },
  "status": "pending" | "in_progress" | "failed" | "completed",
  "metadata": "...",                 // optional opaque string
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:05:00Z"
}
```

### Blueprint (Deployment.config)

```jsonc
{
  "name": "my-app",
  "description": "My application description",
  "source": "remote",               // "remote" | "image"
  "runtime": { /* RuntimeObj */ },
  "remote": { /* RemoteObj */ },
  "run_cmd": "npm start",
  "build_cmd": "npm run build",
  "port": 3000,
  "working_dir": "/app",
  "static_dir": "/app/dist",
  "image": "node:18-alpine",
  "env_vars": {
    "NODE_ENV": "production",
    "PORT": "3000"
  },
  "status": "...",                  // implementation specific
  "project_id": "proj-123"
}
```

List deployments (`GET /deployments`) returns:

```jsonc
{
  "deployments": [ /* Deployment[] */ ],
  "total": 1
}
```

---

## Services

### Service

```jsonc
{
  "id": "01HN2K3M4N5P6Q7R8S9T0U1V2W",
  "name": "my-service",
  "description": "My service description",
  "source": "remote" | "image" | "...",
  "runtime": "nodejs",              // Runtime
  "runtime_version": "18.0.0",
  "run_cmd": "npm start",
  "build_cmd": "npm run build",
  "port": 3000,
  "working_dir": "/app",
  "static_dir": "/app/dist",
  "image": "node:18-alpine",
  "env_vars": {
    "NODE_ENV": "production"
  },
  "status": "running" | "stopped" | "...",
  "remote": "https://github.com/user/repo.git",
  "branch": "main",
  "commit_hash": "abc123def456",
  "blueprint": { /* Blueprint */ },
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:05:00Z"
}
```

List services (`GET /services`) returns:

```jsonc
{
  "services": [ /* Service[] */ ],
  "total": 1
}
```

### ServiceUpdate (PUT/PATCH /services/{serviceId})

```jsonc
{
  "name": "my-service-updated",     // optional
  "description": "Updated description",
  "runtime_version": "20.0.0",
  "run_cmd": "npm start",
  "build_cmd": "npm run build",
  "port": 4000,
  "working_dir": "/app",
  "static_dir": "/app/dist",
  "image": "node:20-alpine",
  "env_vars": {
    "NODE_ENV": "production"
  },
  "branch": "main"
}
```

---

## Logs

### Log stream (GET /logs/stream)

The endpoint returns a `text/event-stream` response. Events look like:

```text
data: cloning repository

data: installing nodejs@18.1.0

: heartbeat

event: done
data: stream completed
```

The SDKs expose this as a raw HTTP response/stream; they do not transform the
individual SSE events.

---

## Proxy

### ProxyStatus (GET /proxy/status)

```jsonc
{
  "status": "running"
}
```

### ProxyRoute (POST /proxy/add)

```jsonc
{
  "domain": "example.com",          // required
  "upstream": "http://localhost:3000" // required
}
```

`POST /proxy/add` responds with a small object:

```jsonc
{
  "message": "Route added successfully"
}
```

`DELETE /proxy/remove` responds similarly when a route is removed.

---

## System

### SystemStatus (GET /system/status)

```jsonc
{
  "status": "healthy" | "degraded" | "unhealthy",
  "uptime": "72h30m15s",
  "services": {
    "total": 5,
    "running": 4,
    "stopped": 1
  },
  "proxy": {
    "status": "running",
    "routes": 3
  }
}
```

### SystemInfo (GET /system/info)

```jsonc
{
  "build": {
    "version": "v0.1.1-beta.17",
    "commit": "a1b2c3d4",
    "build_date": "2024-01-01T12:00:00Z",
    "go_version": "go1.21.0"
  },
  "hardware": {
    "os": "linux",
    "arch": "amd64",
    "cpu_count": 8,
    "hostname": "...",
    "kernel": "Linux 6.8.0-35-generic",
    "mem_total": "7.5Gi",
    "mem_used": "...",
    "mem_free": "...",
    "swap_total": "...",
    "swap_used": "..."
  },
  "storage": {
    "partitions": [
      {
        "filesystem": "/dev/sda1",
        "size": "100Gi",
        "used": "50Gi",
        "available": "50Gi",
        "use_percent": "50%",
        "mountpoint": "/"
      }
    ],
    "devices": [
      {
        "name": "sda",
        "size": "100Gi",
        "type": "disk",
        "mountpoints": ["/"]
      }
    ]
  }
}
```

### SystemDoctorResult (POST /system/doctor, /system/install)

```jsonc
{
  "status": "ok" | "error",
  "output": "combined textual output from scripts",
  "error": "error message if status == 'error'"
}
```

### RegisterInstanceRequest (POST /system/register)

```jsonc
{
  "claim": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", // required: signed claim token issued by base
  "instance_id": "inst_01HXYZABCDEF123456",          // required: unique identifier for this instance
  "issuer": "https://base.dployr.dev",                // optional: expected token issuer
  "audience": "dployr-instance"                       // optional: expected token audience
}
```

---

## Error shapes

Many endpoints use these shared error responses.

### Error

```jsonc
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": { /* optional extra details */ }
}
```

### ValidationError

```jsonc
{
  "error": "Validation failed",
  "details": [
    {
      "field": "name",
      "message": "Field is required"
    }
  ]
}
```
