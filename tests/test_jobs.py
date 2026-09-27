def test_create_job(client, auth_token):
    response = client.post(
        "/jobs/",
        json={
            "company": "Test Company",
            "role": "Test Role",
            "country": "Test Country",
            "status": "Applied",
            "date_applied": "2024-01-01T00:00:00",
            "notes": "Test notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["company"] == "Test Company"
    assert data["role"] == "Test Role"
    assert "id" in data
    assert "user_id" in data

def test_get_jobs(client, auth_token):
    # First, create a job application
    client.post(
        "/jobs/",
        json={
            "company": "Test Company",
            "role": "Test Role",
            "country": "Test Country",
            "status": "Applied",
            "date_applied": "2024-01-01T00:00:00",
            "notes": "Test notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    # Now, retrieve the job applications
    response = client.get(
        "/jobs/",
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_job_by_id(client, auth_token):
    # First, create a job application
    create_response = client.post(
        "/jobs/",
        json={
            "company": "Test Company",
            "role": "Test Role",
            "country": "Test Country",
            "status": "Applied",
            "date_applied": "2024-01-01T00:00:00",
            "notes": "Test notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    job_id = create_response.json()["id"]

    # Now, retrieve the job application by ID
    response = client.get(
        f"/jobs/{job_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == job_id
    assert data["company"] == "Test Company"

def test_update_job(client, auth_token):
    # First, create a job application
    create_response = client.post(
        "/jobs/",
        json={
            "company": "Test Company",
            "role": "Test Role",
            "country": "Test Country",
            "status": "Applied",
            "date_applied": "2024-01-01T00:00:00",
            "notes": "Test notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    job_id = create_response.json()["id"]

    # Now, update the job application
    response = client.put(
        f"/jobs/{job_id}",
        json={
            "company": "Updated Company",
            "role": "Updated Role",
            "country": "Updated Country",
            "status": "Interviewing",
            "date_applied": "2024-02-01T00:00:00",
            "notes": "Updated notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["company"] == "Updated Company"
    assert data["role"] == "Updated Role"

def test_delete_job(client, auth_token):
    # First, create a job application
    create_response = client.post(
        "/jobs/",
        json={
            "company": "Test Company",
            "role": "Test Role",
            "country": "Test Country",
            "status": "Applied",
            "date_applied": "2024-01-01T00:00:00",
            "notes": "Test notes"
        },
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    job_id = create_response.json()["id"]

    # Now, delete the job application
    response = client.delete(
        f"/jobs/{job_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

    # Verify that the job application is deleted
    get_response = client.get(
        f"/jobs/{job_id}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert get_response.status_code == 404