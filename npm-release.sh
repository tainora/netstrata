#!/bin/bash
set -e

# Automatic GitHub token detection for semantic-release based on git config
# Uses git conditional includes to determine which 1Password item to use

# Get 1Password item ID and vault from git config
TOKEN_ID=$(git config --get user.githubToken1PasswordID || echo "")
VAULT_ID=$(git config --get user.githubToken1PasswordVault || echo "")

if [ -z "$TOKEN_ID" ] || [ -z "$VAULT_ID" ]; then
    echo "ERROR: Git config missing GitHub token 1Password credentials"
    echo ""
    echo "Expected git config values:"
    echo "  user.githubToken1PasswordID    (1Password item ID)"
    echo "  user.githubToken1PasswordVault (1Password vault ID)"
    echo ""
    echo "These should be set via git conditional includes in ~/.gitconfig"
    echo "Current directory: $PWD"
    echo "Git config user.name: $(git config --get user.name)"
    echo "Git config user.email: $(git config --get user.email)"
    exit 1
fi

echo "=== Semantic Release with Auto Token Detection ==="
echo "Directory: $PWD"
echo "Git user: $(git config --get user.name) <$(git config --get user.email)>"
echo "Token source: 1Password item $TOKEN_ID"
echo ""

# Retrieve GitHub token from 1Password
echo "Retrieving GitHub token from 1Password..."
GITHUB_TOKEN=$(op item get "$TOKEN_ID" --vault "$VAULT_ID" --fields label=token --reveal)

if [ -z "$GITHUB_TOKEN" ]; then
    echo "ERROR: Failed to retrieve token from 1Password"
    exit 1
fi

echo "Token retrieved successfully"
echo ""

# Run semantic-release with the token
echo "Running semantic-release..."
export GITHUB_TOKEN
export CI=true  # Force production mode (not dry-run)
npm run release
