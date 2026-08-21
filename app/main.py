from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="DevOps Demo Application",
    version="1.0.0",
    description="Automated DevOps and DevSecOps demonstration application",
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>DevOps Demo | Sathvik M M</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, Helvetica, sans-serif;
            }

            body {
                min-height: 100vh;
                background:
                    radial-gradient(circle at top left, #243b55, transparent 40%),
                    radial-gradient(circle at bottom right, #00c6ff, transparent 35%),
                    linear-gradient(135deg, #0f172a, #111827);
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 30px;
            }

            .container {
                width: 100%;
                max-width: 950px;
            }

            .card {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(18px);
                border-radius: 24px;
                padding: 45px;
                box-shadow: 0 25px 70px rgba(0, 0, 0, 0.4);
            }

            .badge {
                display: inline-block;
                padding: 8px 16px;
                border-radius: 30px;
                background: rgba(34, 197, 94, 0.15);
                color: #4ade80;
                border: 1px solid rgba(74, 222, 128, 0.3);
                font-size: 13px;
                font-weight: bold;
                margin-bottom: 20px;
            }

            h1 {
                font-size: 46px;
                line-height: 1.1;
                margin-bottom: 15px;
            }

            .highlight {
                color: #38bdf8;
            }

            .subtitle {
                color: #cbd5e1;
                font-size: 18px;
                line-height: 1.7;
                margin-bottom: 35px;
            }

            .status {
                display: flex;
                align-items: center;
                gap: 12px;
                background: rgba(34, 197, 94, 0.1);
                border: 1px solid rgba(34, 197, 94, 0.25);
                padding: 16px 20px;
                border-radius: 14px;
                margin-bottom: 30px;
            }

            .dot {
                width: 12px;
                height: 12px;
                background: #22c55e;
                border-radius: 50%;
                box-shadow: 0 0 15px #22c55e;
            }

            .status-text {
                color: #86efac;
                font-weight: bold;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
                margin-top: 25px;
            }

            .feature {
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 22px;
                border-radius: 16px;
                transition: transform 0.25s ease,
                            background 0.25s ease;
            }

            .feature:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.1);
            }

            .icon {
                font-size: 28px;
                margin-bottom: 12px;
            }

            .feature h3 {
                margin-bottom: 8px;
                color: #f8fafc;
            }

            .feature p {
                color: #94a3b8;
                font-size: 14px;
                line-height: 1.5;
            }

            .footer {
                margin-top: 35px;
                padding-top: 25px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: #94a3b8;
                font-size: 14px;
            }

            .version {
                color: #38bdf8;
                font-weight: bold;
            }

            @media (max-width: 700px) {
                .card {
                    padding: 30px 22px;
                }

                h1 {
                    font-size: 34px;
                }

                .grid {
                    grid-template-columns: 1fr;
                }

                .footer {
                    flex-direction: column;
                    gap: 10px;
                    text-align: center;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="card">

                <div class="badge">
                    ● AUTOMATED DEVOPS SYSTEM
                </div>

                <h1>
                    Welcome to
                    <span class="highlight">DevOps</span>
                </h1>

                <p class="subtitle">
                    A production-style FastAPI application deployed through
                    Docker, GitHub Actions, Docker Hub and AWS EC2.
                </p>

                <div class="status">
                    <div class="dot"></div>

                    <div>
                        <div class="status-text">
                            Application Running
                        </div>

                        <small>
                            All systems operational
                        </small>
                    </div>
                </div>

                <div class="grid">

                    <div class="feature">
                        <div class="icon">🐳</div>

                        <h3>Docker</h3>

                        <p>
                            Containerized application running
                            with a lightweight Python environment.
                        </p>
                    </div>

                    <div class="feature">
                        <div class="icon">⚙️</div>

                        <h3>CI/CD</h3>

                        <p>
                            Automated testing, image building
                            and deployment using GitHub Actions.
                        </p>
                    </div>

                    <div class="feature">
                        <div class="icon">☁️</div>

                        <h3>AWS EC2</h3>

                        <p>
                            Application deployed on an Ubuntu
                            cloud server behind Nginx.
                        </p>
                    </div>

                    <div class="feature">
                        <div class="icon">🔐</div>

                        <h3>DevSecOps</h3>

                        <p>
                            Security-conscious deployment architecture
                            with controlled SSH access.
                        </p>
                    </div>

                    <div class="feature">
                        <div class="icon">📊</div>

                        <h3>Health Monitoring</h3>

                        <p>
                            Docker health checks and FastAPI health
                            endpoints monitor application status.
                        </p>
                    </div>

                    <div class="feature">
                        <div class="icon">🚀</div>

                        <h3>Automated Deployment</h3>

                        <p>
                            Every update can automatically move from
                            GitHub to the production server.
                        </p>
                    </div>

                </div>

                <div class="footer">
                    <div>
                        Built by <strong>Sathvik M M</strong>
                    </div>

                    <div>
                        DevSecOps Engineer
                        <span class="version">• v1.0.0</span>
                    </div>
                </div>

            </div>

        </div>

    </body>
    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }