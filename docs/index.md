<!--<!DOCTYPE html>-->
<html>
<head>
  <meta charset="UTF-8">
  <title>Kaotic Fire Backuptools</title>
  <link rel="icon" href="assets/favicon.ico" type="image/x-icon">
  <link href="https://cdn.jsdelivr.net/npm/prismjs/themes/prism-okaidia.min.css" rel="stylesheet" />
  <script src="https://cdn.jsdelivr.net/npm/prismjs/prism.js"></script>
  <style>
    body.dark-mode {
        background-color: #121212;
        color: #e0e0e0;
    }
    .toggle-btn {
        position: fixed;
        top: 1rem;
        right: 1rem;
        background: #f05030;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        cursor: pointer;
        font-weight: bold;
    }
    </style>
    <script>
    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    }
    window.onload = function() {
        if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        }
    };
    </script>
</head>
<body>
    <button class="toggle-btn" onclick="toggleDarkMode()">🌗 Toggle Dark Mode</button>
  <div style="text-align: center;">
    <img src="assets/logo.svg" alt="Kaotic Fire Logo" width="150">
    <h1>Kaotic Fire: Backuptools</h1>
    <p><strong>Version:</strong> 1.0.0<br><strong>Author:</strong> Kaotic Fire</p>
    <p>Automated backup roles for containers and desktops — Galaxy-ready, CI-tested, semver-tracked.</p>
  </div>

  <hr>

  <h2>🔥 Install</h2>
  <pre><code class="language-shell">ansible-galaxy collection install kaoticfire.backuptools</code></pre>

  <h2>🧪 CI Status</h2>
  <p>
    <img src="https://github.com/kaoticfire/ansible-collection-backuptools/actions/workflows/test.yml/badge.svg">
  </p>

  <h2>💻 Example Usage</h2>
  <pre><code class="language-yaml">
- name: Desktop Backup
  hosts: localhost
  become: true
  roles:
    - role: kaoticfire.backuptools.desktop_backup
      vars:
        desktop_backup_include:
          - "$HOME/Documents"
          - "$HOME/Pictures"
        desktop_backup_exclude:
          - "**/node_modules"
          - "**/.cache"
        desktop_backup_time: "03:00"
  </code></pre>

  <hr>
    <p style="text-align: center;">
      <a href="changelog.md">View Changelog</a>
    </p>
  <p style="text-align: center;">
    🔥 Built with grit by Kaotic Fire — view on <a href="https://github.com/kaoticfire/ansible-collection-backuptools">GitHub</a>
  </p>
</body>
</html>
