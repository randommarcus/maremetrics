from app.models.profile import ProfileSummary


def transform_profiles(raw_profiles):

    transformed = []

    for profile in raw_profiles:

        coordinates = profile["geolocation"]["coordinates"]

        transformed.append(
            ProfileSummary(
                profile_id=profile["_id"],
                timestamp=profile["timestamp"],
                latitude=coordinates[1],
                longitude=coordinates[0],
                cycle_number=profile["cycle_number"],
                profile_direction=profile["profile_direction"]
            )
        )

    return transformed