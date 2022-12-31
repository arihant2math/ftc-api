""" Contains all the data models used in inputs/outputs """

from .alliance import Alliance
from .alliance_selection import AllianceSelection
from .alliance_selection_details import AllianceSelectionDetails
from .api_information import APIInformation
from .auto_navigated_status import AutoNavigatedStatus
from .auto_navigation import AutoNavigation
from .award import Award
from .award_assignment import AwardAssignment
from .award_assignment_list import AwardAssignmentList
from .award_list import AwardList
from .barcode_element import BarcodeElement
from .endgame_parked_status import EndgameParkedStatus
from .event import Event
from .event_list import EventList
from .event_ranking_list import EventRankingList
from .field_side import FieldSide
from .freight_frenzy_alliance_score_breakdown import FreightFrenzyAllianceScoreBreakdown
from .freight_frenzy_alliance_score_details import FreightFrenzyAllianceScoreDetails
from .freight_frenzy_remote_score_breakdown import FreightFrenzyRemoteScoreBreakdown
from .freight_frenzy_single_team_score_details import FreightFrenzySingleTeamScoreDetails
from .ftc_event_level import FTCEventLevel
from .get_v20_season_schedule_event_code_tournament_level_hybrid_tournament_level import (
    GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel,
)
from .get_v20_season_scores_event_code_tournament_level_tournament_level import (
    GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel,
)
from .hybrid_schedule import HybridSchedule
from .hybrid_schedule_match import HybridScheduleMatch
from .hybrid_schedule_team import HybridScheduleTeam
from .junction_element import JunctionElement
from .league import League
from .league_list import LeagueList
from .league_members import LeagueMembers
from .match_result import MatchResult
from .match_result_list import MatchResultList
from .match_result_team import MatchResultTeam
from .match_score_list import MatchScoreList
from .power_play_alliance_score_breakdown import PowerPlayAllianceScoreBreakdown
from .power_play_alliance_score_details import PowerPlayAllianceScoreDetails
from .power_play_remote_score_breakdown import PowerPlayRemoteScoreBreakdown
from .power_play_single_team_score_details import PowerPlaySingleTeamScoreDetails
from .scheduled_match import ScheduledMatch
from .scheduled_match_list import ScheduledMatchList
from .scheduled_match_team import ScheduledMatchTeam
from .season_summary import SeasonSummary
from .selection import Selection
from .selection_result import SelectionResult
from .sky_stone_alliance_score_details import SkyStoneAllianceScoreDetails
from .sky_stone_score_details import SkyStoneScoreDetails
from .stone import Stone
from .summary_championship_description import SummaryChampionshipDescription
from .team import Team
from .team_list import TeamList
from .team_ranking import TeamRanking
from .ultimate_goal_alliance_score_breakdown import UltimateGoalAllianceScoreBreakdown
from .ultimate_goal_alliance_score_details import UltimateGoalAllianceScoreDetails
from .ultimate_goal_single_team_breakdown import UltimateGoalSingleTeamBreakdown
from .ultimate_goal_single_team_score_details import UltimateGoalSingleTeamScoreDetails

__all__ = (
    "Alliance",
    "AllianceSelection",
    "AllianceSelectionDetails",
    "APIInformation",
    "AutoNavigatedStatus",
    "AutoNavigation",
    "Award",
    "AwardAssignment",
    "AwardAssignmentList",
    "AwardList",
    "BarcodeElement",
    "EndgameParkedStatus",
    "Event",
    "EventList",
    "EventRankingList",
    "FieldSide",
    "FreightFrenzyAllianceScoreBreakdown",
    "FreightFrenzyAllianceScoreDetails",
    "FreightFrenzyRemoteScoreBreakdown",
    "FreightFrenzySingleTeamScoreDetails",
    "FTCEventLevel",
    "GetV20SeasonScheduleEventCodeTournamentLevelHybridTournamentLevel",
    "GetV20SeasonScoresEventCodeTournamentLevelTournamentLevel",
    "HybridSchedule",
    "HybridScheduleMatch",
    "HybridScheduleTeam",
    "JunctionElement",
    "League",
    "LeagueList",
    "LeagueMembers",
    "MatchResult",
    "MatchResultList",
    "MatchResultTeam",
    "MatchScoreList",
    "PowerPlayAllianceScoreBreakdown",
    "PowerPlayAllianceScoreDetails",
    "PowerPlayRemoteScoreBreakdown",
    "PowerPlaySingleTeamScoreDetails",
    "ScheduledMatch",
    "ScheduledMatchList",
    "ScheduledMatchTeam",
    "SeasonSummary",
    "Selection",
    "SelectionResult",
    "SkyStoneAllianceScoreDetails",
    "SkyStoneScoreDetails",
    "Stone",
    "SummaryChampionshipDescription",
    "Team",
    "TeamList",
    "TeamRanking",
    "UltimateGoalAllianceScoreBreakdown",
    "UltimateGoalAllianceScoreDetails",
    "UltimateGoalSingleTeamBreakdown",
    "UltimateGoalSingleTeamScoreDetails",
)
