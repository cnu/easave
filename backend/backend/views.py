import logging

from flask import (
    Blueprint,
    render_template,
    request,
    current_app as app,
    current_app,
    jsonify,
)

# from backend.extensions import db
from backend.models import User, Business, Deposit, Loan
from backend.extensions import firebase

# firebase_request_adapter = requests.Request()
bp = Blueprint("backend", __name__, url_prefix="/api")

log = logging.getLogger(__name__)


@bp.route("/user/", methods=["POST"])
@firebase.jwt_required
def user_login():
    """Logs in a user or registers a new user.

    Returns back whether the user is a known one or a new one.
    """
    """
    {
        "kind": "identitytoolkit#VerifyPasswordResponse",
        "localId": "B6zEjAp69PRPh9L036TLyVxouNM2",
        "email": "test@gmail.com",
        "displayName": "",
        "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc2MDI3MTI2ODJkZjk5Y2ZiODkxYWEwMzdkNzNiY2M2YTM5NzAwODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaGFja3RpdmF0b3JzLTdkYzcwIiwiYXVkIjoiaGFja3RpdmF0b3JzLTdkYzcwIiwiYXV0aF90aW1lIjoxNzE1NDQzNDUzLCJ1c2VyX2lkIjoiQjZ6RWpBcDY5UFJQaDlMMDM2VEx5VnhvdU5NMiIsInN1YiI6IkI2ekVqQXA2OVBSUGg5TDAzNlRMeVZ4b3VOTTIiLCJpYXQiOjE3MTU0NDM0NTMsImV4cCI6MTcxNTQ0NzA1MywiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ0ZXN0QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.WwnPxBcGwnk7b2suKKibfGnp2W3US6hYlAQ8QkW9fwKb9hv8rV54nd1B_G9_UGYmFdfdsG1fbbcS-IYgniWejw5olSsyHRRmRXczcSlfYf70oQP7R457Yr_iOZHcH-yMBLWgYxhaYRzupw2kvs3QBtnGjIvh4vagmdHVVxmJCDEmIJyWc1JqN2NfVj_ZWQ-w0D2M6A90QMIYInAZZtnhcx4oafyQbiqObavDz9x3z2eGDwPGuUXsVDWfvYfJ7SW-QF-hj9NUhiRor-kXV7svFf_1xhKFLf-bMxz1ZriTXA9MPxVHJI-YU-Vn49KCbXgo6BOpeHETcDKGNCPBnXd9Ng",
        "registered": true,
        "refreshToken": "AMf-vBx19eNSfgAs-Ptw9rgfgFwGLZwue5P5AuPKxlJk6ny9pn6WRjXn7GL2WtISE3qTK7KYSAEXFxbvv0Ev6f0DvLOOQmQnoiLv8syfam3z-MRr08dWzMAUhxwMR5q526roeQdjTFYFrTSZ3zKYPqQKsRPC2EN-Kx2_5EMwlwSuHynkV6Kg3srCCwtiMHYjH1bIGipAldLN-IsZMOvdP309SyVdCxQ9Eg",
        "expiresIn": "3600"
    }
    """
    try:
        log.info(request.jwt_payload)
        log.info(request.jwt_payload["email"])
        user = User.query.filter_by(email=request.jwt_payload["email"]).first()
        if user:
            return {"known": True}
        else:
            user = User(
                email=request.jwt_payload["email"],
                uid=request.jwt_payload["uid"],
            )
            user.save()
            return {"known": False}
    except ValueError as e:
        error_message = str(e)
        return {"error": error_message}


@bp.route("/business/", methods=["POST", "GET"])
@firebase.jwt_required
def create_or_get_business():
    """Creates a new business for the user."""
    if request.method == "GET":
        user = User.query.filter_by(email=request.jwt_payload["email"]).first()
        businesses = Business.query.filter_by(user_id=user.id).all()
        return jsonify(businesses)
    else:
        try:
            user = User.query.filter_by(email=request.jwt_payload["email"]).first()
            name = request.json["name"]
            industry = request.json["industry"]
            pan = request.json["pan"]
            address = request.json["address"]
            gstin = request.json["gstin"]
            business = Business(
                name=name,
                industry=industry,
                pan=pan,
                address=address,
                gstin=gstin,
                user_id=user.id,
            )
            business.save()
            return jsonify(business)
        except ValueError as e:
            error_message = str(e)
            return {"error": error_message}


@bp.route("/deposit/", methods=["POST", "GET"])
def create_or_get_deposit():
    """Creates a new deposit for the user."""
    if request.method == "GET":
        business_id = request.json["business_id"]
        # get deposits for a business sorted by created_at reverse
        deposits = (
            Deposit.query.filter_by(business_id=business_id)
            .order_by(Deposit.created_at.desc())
            .all()
        )
        return jsonify(deposits)
    else:
        try:
            amount = request.json["amount"]
            business_id = request.json["business_id"]
            deposit = Deposit(amount=amount, business_id=business_id)
            deposit.save()
            return jsonify(deposit)
        except ValueError as e:
            error_message = str(e)
            return {"error": error_message}


@bp.route("/loan/", methods=["POST", "GET"])
def create_or_get_loan():
    """Creates a new loan for the user."""
    if request.method == "GET":
        business_id = request.json["business_id"]
        loans = Loan.query.filter_by(business_id=business_id)
        return jsonify(loans)
    else:
        try:
            amount = request.json["amount"]
            business_id = request.json["business_id"]
            # check if business doesn't already have a loan
            existing_loan = Loan.query.filter_by(business_id=business_id).all()
            if existing_loan:
                return {"error": "Business already has a loan."}
            loan = Loan(amount=amount, business_id=business_id)
            loan.save()
            return jsonify(loan)
        except ValueError as e:
            error_message = str(e)
            return {"error": error_message}


@bp.route("/loan/allowed/", methods=["GET"])
def allowed_loan():
    business_id = request.json["business_id"]
    existing_loan = Loan.query.all(business_id=business_id)
    if existing_loan:
        return {"error": "Business already has a loan."}
    else:
        # calculate the allowed loan amount
        pass
    return {"allowed": 100_000}
