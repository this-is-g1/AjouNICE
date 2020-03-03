// 게시물
import modPost from './post/modPost.graphql'
import modReply from './post/modReply.graphql'
import IncrementViewCount from './post/incrementView.graphql'
// Will be deprecated
import writeReply from './post/writeReply.graphql'
import editReply from './post/editReply.graphql'
import removeReply from './post/removeReply.graphql'
import writePost from './post/writePost.graphql'
import editPost from './post/editPost.graphql'
import removePost from './post/removePost.graphql'

// 인증
import LoggedInLogger from './auth/LoggedInLogger.graphql'
import Authorize from './auth/Authorize.graphql'

// 관리자
import addCategory from './admin/addCategory.graphql'
import removeCategory from './admin/removeCategory.graphql'
import addGourmetPlace from './admin/addGourmetPlace.graphql'
import removeGourmet from './admin/removeGourmet.graphql'
import modCollege from './admin/modCollege.graphql'
import modDepartment from './admin/modDepartment.graphql'
import createCollege from './admin/createCollege.graphql'
import createDepartment from './admin/createDepartment.graphql'

// 파일 업로드 트리거
import singleUpload from './upload/singleUpload.graphql'
import multiUpload from './upload/multiUpload.graphql'

export {
  modPost,
  modReply,
  IncrementViewCount,
  writeReply,
  removeReply,
  editReply,
  writePost,
  editPost,
  removePost,
  LoggedInLogger,
  Authorize,
  addCategory,
  removeCategory,
  addGourmetPlace,
  removeGourmet,
  modCollege,
  modDepartment,
  createCollege,
  createDepartment,
  singleUpload,
  multiUpload
}
